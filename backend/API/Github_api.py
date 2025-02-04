import os
import sqlite3
from datetime import datetime, timezone
from typing import List, Any
import github
from github import Github, Auth
from . import SQL_api
def get_github_connection() -> Github:
    # Function to connect to Github API
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")
    with open(keys_path, "r") as file:
        key = file.readline().strip()
    auth = Auth.Token(key)
    return Github(auth=auth)

def update_required(git: Github, conn: sqlite3.Connection, author: str, repo_name: str) -> bool: 
    # Get cut_off_date
    cursor = conn.cursor()
    cut_off_date = SQL_api.get_project_update(conn, author, repo_name)

    # Get repository
    repo = git.get_repo(f"{author}/{repo_name}")
    cut_off_date = cut_off_date.replace(tzinfo=timezone.utc)

    # Fetch the most recent commit date
    most_recent = repo.get_commits()[0].commit.author.date
    if cut_off_date > most_recent:  # No (more) new commits
        return False

    return True

def grab_commits(git: Github, conn: sqlite3.Connection, author: str, repo_name: str) -> List[List]: 
    repo = git.get_repo(f"{author}/{repo_name}")
    branches = repo.get_branches()
    selected_branch = branches[0].name
    
    if any(branch.name == "main" for branch in branches):
        selected_branch = "main"
    elif any(branch.name == "master" for branch in branches):
        selected_branch = "master"

    try:
        # Fetch commits from selected branch
        cut_off_datetime = SQL_api.get_project_update(conn, author, repo_name)
        commits = repo.get_commits(sha=selected_branch, since=cut_off_datetime)
        if commits.totalCount == 0:
            raise ValueError("No commits found in master branch")
        else:
            return parse_commits(repo, commits)
    except ValueError:  # If no commits in master, fallback to 'main'
        pass

def parse_commits(repo: github.Repository, commits: github.Commit):
    # Iterate through commits
    commit_date = repo.get_commits()[0].commit.author.date.date()
    selected_commits = []
    cur = []
    for commit in commits:
        if commit_date != commit.commit.author.date.date():  
            selected_commits.append(cur)
            commit_date = commit.commit.author.date.date()
            cur = [commit]
        else:
            cur.append(commit)
    selected_commits.append(cur)
    return selected_commits

def parse_files(git: Github, author: str, repo_name: str, commits_array: List[List[Any]]) -> List[List[Any]]: # ContentFile[][]: files to run, organized by date 
    repo = git.get_repo(f"{author}/{repo_name}")
    target_file_extension = {".java"}
    files = []
    for commits in commits_array:
        files_items = []
        marked = set()  # Tracks files that have already been added

        try:
            if not commits:
                raise ValueError("Empty commit batch found. Skipping this batch.")

            for commit in commits:
                for file in commit.files:
                    filename = file.filename
                    if os.path.splitext(filename)[1] in target_file_extension:
                        if file.status != "removed" and filename not in marked:
                            files_items.append(repo.get_contents(filename, ref=commit.sha))
                            marked.add(filename)  # Mark file as processed

        except ValueError as e:
            print(f"Warning: {e}")  # Log the error and continue instead of stopping
            continue  # Skip this commit batch and move to the next one
        if len(files_items) > 0:
            files.append([commits[0].commit.author.date.date(), files_items])


    # First item in each is the date of the files, with the following items being the ContentFiles
    return files
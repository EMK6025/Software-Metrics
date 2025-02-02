import os
from datetime import datetime, timezone
from typing import List, Any
import github
from github import Github, Auth

def get_github_connection() -> Github:
    # Function to connect to Github API
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")
    with open(keys_path, "r") as file:
        key = file.readline().strip()
    auth = Auth.Token(key)
    return Github(auth=auth)

def update_required(git: Github, author: str, repo_name: str, cut_off_date: datetime) -> bool: 

    #If no new git commits, update last_update timestamp for project 

    # Get repository
    repo = git.get_repo(f"{author}/{repo_name}")
    cut_off_date = cut_off_date.replace(tzinfo=timezone.utc)

    # Fetch the most recent commit date
    cur_date = repo.get_commits()[0].commit.author.date
    if cut_off_date > cur_date:  # No (more) new commits
        return False
    
    return True

def grab_commits(git: Github, author: str, repo_name: str, cut_off_date: datetime) -> List[List]: 
    repo = git.get_repo(f"{author}/{repo_name}")
    branches = repo.get_branches()
    selected_branch = branches[0].name
    
    if any(branch.name == "main" for branch in branches):
        selected_branch = "main"
    elif any(branch.name == "master" for branch in branches):
        selected_branch = "master"

    try:
        # Fetch commits from selected branch
        commits = repo.get_commits(sha=selected_branch, since=cut_off_date)
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

            files.append([commits[0].commit.author.date.date(), files_items])

        except ValueError as e:
            print(f"Warning: {e}")  # Log the error and continue instead of stopping
            continue  # Skip this commit batch and move to the next one

    # First item in each is the date of the files, with the following items being the ContentFiles
    return files

if __name__ == "__main__":
    author = "EMK6025"
    repo = "Software-Metrics"
    cut_off_date = datetime.strptime("2025-01-23 00:00:00", "%Y-%m-%d %H:%M:%S")

    if update_required(author, repo, cut_off_date):
        commits = grab_commits(author, repo, cut_off_date)
        parse_files(author, repo, commits)
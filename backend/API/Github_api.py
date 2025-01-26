from github import Github, Auth
import os
from datetime import datetime, timezone

def update_required(author, repo_name, cut_off_date): # Boolean: whether or not an update is required
    # Grabbing file path to keys.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")

    # Reading private access token
    with open(keys_path, "r") as file:
        key = file.readline().strip()

    # Public Web Github
    auth = Auth.Token(key)
    g = Github(auth=auth)

    # Get repository
    repo = g.get_repo(f"{author}/{repo_name}")

    cut_off_date = cut_off_date.replace(tzinfo=timezone.utc)

    cur_date = repo.get_commits()[0].commit.author.date # Grab time of most recent commit
    if cut_off_date > cur_date: # No (more) new commits
        g.close()
        return False
    
    g.close()
    return True

def grab_commits(author, repo_name, cut_off_date): # 2D Array of Commits: parses for new commits
    # Connecting to repo boilerplate for Github API
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")
    with open(keys_path, "r") as file:
        key = file.readline().strip()
    auth = Auth.Token(key)
    g = Github(auth=auth)
    repo = g.get_repo(f"{author}/{repo_name}")\
    
    # Parse for new commits, sorted by dates
    cut_off_date = cut_off_date.date()
    cur_date = repo.get_commits()[0].commit.author.date.date()
    selected_commit_arrays = []
    selected_commits = []

    # Iterate through commits
    for commit in repo.get_commits():
        commit_date = commit.commit.author.date.date() 
        if cut_off_date > commit_date: # no (more) new commits
            return selected_commit_arrays

        if cur_date == commit_date: # more commits on the same calendar date
            selected_commits.append(commit)
        else:
            cur_date = commit_date
            selected_commit_arrays.append(selected_commits)
            selected_commits = [commit]

    g.close()

if __name__ == "__main__":
    date = "2025-01-01 00:00:00"
    cut_off_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    update_required("EMK6025", "Software-Metrics", cut_off_date)
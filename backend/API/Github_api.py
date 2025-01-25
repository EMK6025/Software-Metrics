from github import Github, Auth
import os
from datetime import datetime, timezone

def update_required(author, repo_name, cut_off_date):
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
    last_commit_date = repo.get_commits()[0].commit.author.date.replace(tzinfo=timezone.utc)

    if cut_off_date > last_commit_date: # no new commits
        return False 
    
    # Iterate through commits
    for commit in repo.get_commits():
        print(commit.commit.author.date)
        print(commit.commit.message)
        print("Modified Files: ")
        for file in commit.files:
            print(file.filename)
        print()

    # Close connection
    g.close()

if __name__ == "__main__":
    update_required("EMK6025", "Software-Metrics", datetime.now())
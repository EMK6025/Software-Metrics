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

    cur_date = repo.get_commits()[0].commit.author.date # Grab time of most recent commit
    if cut_off_date > cur_date: # No (more) new commits
        g.close()
        return False
    
    g.close()
    return True

if __name__ == "__main__":
    date = "2025-01-01 00:00:00"
    cut_off_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    update_required("EMK6025", "Software-Metrics", cut_off_date)
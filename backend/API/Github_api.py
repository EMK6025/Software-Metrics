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

def grab_commits(author, repo_name, cut_off_date): # Commit[]: parses for new commits #FIX - NEED TO PARSE FOR ALL JAVA PROGRAMS
    # Connecting to repo boilerplate for Github API
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")
    with open(keys_path, "r") as file:
        key = file.readline().strip()
    auth = Auth.Token(key)
    g = Github(auth=auth)
    repo = g.get_repo(f"{author}/{repo_name}")
    
    # Parse for new commits, sorted by dates
    cut_off_date = cut_off_date.date()
    commit_date = repo.get_commits()[0].commit.author.date.date()
    selected_commits = [repo.get_commits()[0]]

    # Iterate through commits
    for commit in repo.get_commits():
        if cut_off_date > commit_date: # no (more) new commits
            g.close()
            return selected_commits
        # only need latest commit for each calendar date
        if commit_date != commit.commit.author.date.date():  
            # commit is on a different date, and also needs to be processed
            commit_date = commit.commit.author.date.date()
            selected_commits.append(commit)

    g.close()

def parse_files(author, repo_name, commits): # ContentFile[][]: files to run, organized by date 
    # First item in each is the date of the files, with the following items being the ContentFiles
    # Connecting to repo boilerplate for Github API
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keys_path = os.path.join(script_dir, "keys.txt")
    with open(keys_path, "r") as file:
        key = file.readline().strip()
    auth = Auth.Token(key)
    g = Github(auth=auth)
    repo = g.get_repo(f"{author}/{repo_name}")
    target_file_extension = {".java", ".css"}
    files = []

    for commit in commits:
        files_items = []
        for file in commit.files:
            if os.path.splitext(file.filename)[1] in target_file_extension:
                if file.status != "removed": # Only attempt to get contents if the file was not deleted
                    files_items.apphend(repo.get_contents(file.filename, ref=commit.sha))
                #     decoded_content = base64.b64decode(file_content.content).decode('utf-8')
        files.apphend([commit.commit.author.date.date(), files_items])
    return files


if __name__ == "__main__":
    author = "EMK6025"
    repo = "Software-Metrics"
    cut_off_date = datetime.strptime("2025-01-23 00:00:00", "%Y-%m-%d %H:%M:%S")

    if update_required(author, repo, cut_off_date):
        commits = grab_commits(author, repo, cut_off_date)
        parse_files(author, repo, commits)
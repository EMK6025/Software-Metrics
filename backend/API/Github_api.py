from github import Github, Auth
import os

# Grabbing file path to keys.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
keys_path = os.path.join(script_dir, "keys.txt")

# Reading private access token
with open(keys_path, "r") as file:
            key = file.readline().strip()

auth = Auth.Token(key)

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()
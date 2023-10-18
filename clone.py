import git
import os

# Define the SSH URL of the Git repository to clone
repository_url = "git@github.com:sachin93094/private_Repo.git"

# Directory where you want to clone the repository
clone_directory = "private_Repo"

# Clone the repository
if not os.path.exists(clone_directory):
    git.Repo.clone_from(repository_url, clone_directory)
    print(f"Repository cloned successfully.")
else:
    print(f"Repository '{clone_directory}' already exists. Skipping clone.")

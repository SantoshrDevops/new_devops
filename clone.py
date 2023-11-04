import subprocess
import git
import os

# Define your Git identity (update with your information)
git_name = "sachin93093"
git_email = "sachin93093@gmail.com"

# Set your Git identity globally
subprocess.check_call(["git", "config", "--global", "user.name", git_name])
subprocess.check_call(["git", "config", "--global", "user.email", git_email])

# Define the HTTP URL of the first Git repository to clone
# Retrieve username and Personal Access Token from TeamCity environment variables
username = os.environ.get('GITHUB_USERNAME')
token = os.environ.get('GITHUB_TOKEN')

if not username or not token:
    print("GitHub username and token environment variables are not set.")
    exit(1)

# Construct the repository URL with the Personal Access Token
repository_url1 = f"https://{username}:{token}@github.com/sachin93094/private_Repo.git"

# Define the directory to clone the first repository
clone_directory1 = "private_Repo"

# Clone the first repository
try:
    subprocess.check_call(["git", "clone", repository_url1, clone_directory1])
    print(f"Repository '{clone_directory1}' cloned successfully.")
except subprocess.CalledProcessError as e:
    print(f"Repository cloning failed: {e}")

# Get the latest tag for the first repository
repo1 = git.Repo(clone_directory1)

try:
    latest_tag1 = repo1.git.describe(tags=True, abbrev=0)
    print(f"Latest tag for '{clone_directory1}': {latest_tag1}")
except git.exc.GitCommandError as e:
    print(f"Error getting the latest tag for '{clone_directory1}': {e}")

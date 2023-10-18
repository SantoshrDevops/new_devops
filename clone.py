import subprocess
import git

# Define the SSH URL of the first Git repository to clone
repository_url1 = "git@github.com:sachin93094/private_Repo.git"
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

# Define the SSH URL of the second Git repository to clone
repository_url2 = "git@github.com:sachin93094/git_remote_demorepo1.git"
clone_directory2 = "git_remote_demorepo1"

# Clone the second repository
try:
    subprocess.check_call(["git", "clone", repository_url2, clone_directory2])
    print(f"Repository '{clone_directory2}' cloned successfully.")
except subprocess.CalledProcessError as e:
    print(f"Repository cloning failed: {e}")

# Get the latest tag for the second repository
repo2 = git.Repo(clone_directory2)

try:
    latest_tag2 = repo2.git.describe(tags=True, abbrev=0)
    print(f"Latest tag for '{clone_directory2}': {latest_tag2}")
except git.exc.GitCommandError as e:
    print(f"Error getting the latest tag for '{clone_directory2}': {e}")

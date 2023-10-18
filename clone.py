import subprocess

# Define the SSH URL of the Git repository to clone
repository_url = "git@github.com:sachin93094/private_Repo.git"

# Directory where you want to clone the repository
clone_directory = "private_Repo"

# Clone the repository
try:
    subprocess.check_call(["git", "clone", repository_url, clone_directory])
    print("Repository cloned successfully in teamcity.")
except subprocess.CalledProcessError as e:
    print(f"Repository cloning failed: {e}")

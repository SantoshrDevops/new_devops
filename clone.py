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

# Define the SSH URL of the second Git repository to clone
repository_url2 = "git@github.com:sachin93094/git_remote_demorepo1.git"
clone_directory2 = "git_remote_demorepo1"

# Clone the second repository
try:
    subprocess.check_call(["git", "clone", repository_url2, clone_directory2])
    print(f"Repository '{clone_directory2}' cloned successfully.")
except subprocess.CalledProcessError as e:
    print(f"Repository cloning failed: {e}")

# Define the SSH URL of the third Git repository to clone
repository_url3 = "git@github.com:sachinsdevops/sample_teamcity.git"
clone_directory3 = "sample_teamcity"

# Clone the third repository
try:
    subprocess.check_call(["git", "clone", repository_url3, clone_directory3])
    print(f"Repository '{clone_directory3}' cloned successfully.")
except subprocess.CalledProcessError as e:
    print(f"Repository cloning failed: {e}")

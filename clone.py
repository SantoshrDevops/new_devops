import subprocess
import git
import os  # Import the os module to access environment variables

if not os.path.exists(clone_directory2):
    os.makedirs(clone_directory2)
# Define your Git identity (update with your information)
git_name = "sachin93093"
git_email = "sachin93093@gmail.com"

# Set your Git identity globally
subprocess.check_call(["git", "config", "--global", "user.name", git_name])
subprocess.check_call(["git", "config", "--global", "user.email", git_email])

# Define the HTTP URL of the first Git repository to clone
# Retrieve username and password from TeamCity environment variables
username = os.environ.get('username')  # Replace 'TC_USERNAME' with your actual environment variable name
password = os.environ.get('password')  # Replace 'TC_PASSWORD' with your actual environment variable name

# Construct the repository URL with credentials
repository_url1 = f"https://{username}:{password}@github.com/sachin93094/private_Repo.git"

# Update with the HTTP URL and use the constructed repository URL
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

# Define the HTTP URL of the second Git repository to clone
# Retrieve the username and password from TeamCity environment variables
username = os.environ.get('TC_USERNAME')  # Replace 'TC_USERNAME' with your actual environment variable name
password = os.environ.get('TC_PASSWORD')  # Replace 'TC_PASSWORD' with your actual environment variable name

# Construct the repository URL with credentials
repository_url2 = f"https://{username}:{password}@github.com/sachin93094/git_remote_demorepo1.git"

# Update with the HTTP URL and use the constructed repository URL
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

# Define the name of the new tag
new_tag_name = "v3.0.0"

# Create and push the new tag for the first repository
try:
    tag1 = repo1.create_tag(new_tag_name, message="Created a new tag")
    remote1 = repo1.create_remote('origin', repository_url1)  # Add the HTTP URL as the remote
    remote1.push("--tags")
    print(f"Created and pushed tag '{new_tag_name}' for '{clone_directory1}'")
except git.exc.GitCommandError as e:
    print(f"Error creating/pushing the tag for '{clone_directory1}': {e}")

# Create and push the new tag for the second repository
try:
    tag2 = repo2.create_tag(new_tag_name, message="Created a new tag")
    remote2 = repo2.create_remote('origin', repository_url2)  # Add the HTTP URL as the remote
    remote2.push("--tags")
    print(f"Created and pushed tag '{new_tag_name}' for '{clone_directory2}'")
except git.exc.GitCommandError as e:
    print(f"Error creating/pushing the tag for '{clone_directory2}': {e}")

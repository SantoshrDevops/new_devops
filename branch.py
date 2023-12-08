import subprocess
import sys

def get_latest_git_branch():
    try:
        # Set the remote repository URL with the personal access token
        remote_url = 'https://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@github.com/sachinsdevops/sample_teamcity.git'

        # Set up the Git remote with the URL
        subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)

        # Fetch all remote branches
        subprocess.run(['git', 'fetch', '--all'], check=True)

        # Command to get the latest branch name
        command = 'git for-each-ref --sort=-committerdate --format "%(refname:short)" refs/remotes/origin/ | head -n 1'

        # Run the command and capture the output
        latest_branch = subprocess.check_output(command, shell=True, universal_newlines=True).strip()

        return latest_branch
    except subprocess.CalledProcessError as e:
        print(f"Error fetching remote branches: {e}")
        sys.exit(1)

def checkout_latest_branch():
    try:
        # Get the latest Git branch
        latest_branch = get_latest_git_branch()

        if latest_branch:
            # Print the selected branch for TeamCity parameter
            print(f"##teamcity[setParameter name='latestBranch' value='{latest_branch}']")
            
            # Remove 'origin/' prefix if present
            branch_name = latest_branch.split('/', 1)[-1]

            # Checkout the latest branch
            subprocess.run(['git', 'checkout', '-b', branch_name, f'remotes/origin/{latest_branch}'], check=True)
            print(f"Checked out latest branch: {latest_branch}")
        else:
            print("Failed to determine the latest branch.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running Git command: {e}")
        sys.exit(1)

if __name__ == "__main__":
    checkout_latest_branch()

import os
import subprocess

# Define the file to be removed and the .gitignore path
secret_file = "toolbinge-log-firebase-adminsdk-ol9rx-3d911b209f.json"
gitignore_path = ".gitignore"


# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)


# Step 1: Remove the secret file from the current commit
run_command(f"git rm --cached {secret_file}")

# Step 2: Add the secret file to .gitignore
with open(gitignore_path, "a") as gitignore:
    gitignore.write(f"\n{secret_file}\n")

# Step 3: Commit the changes
run_command("git add .gitignore")
run_command('git commit -m "Remove service account key and update .gitignore"')

# Step 4: Use BFG Repo-Cleaner to remove the file from the repository history
bfg_command = f"bfg --delete-files {secret_file}"
print(f"Running BFG Repo-Cleaner command: {bfg_command}")
run_command(bfg_command)

# Step 5: Clean up the Git history
run_command("git reflog expire --expire=now --all")
run_command("git gc --prune=now --aggressive")

# Step 6: Force push the changes to the repository
run_command("git push origin --force")

print("Secret file removed and repository cleaned.")

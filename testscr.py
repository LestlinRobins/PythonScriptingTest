import os
import subprocess
from datetime import datetime, timedelta

# === HARD-CODED VALUES (EDIT THESE) ===
num_commits = 10  # Number of commits you want to make
start_date = datetime(2024, 6, 1, 12, 0, 0)  # Start date (YYYY, MM, DD, HH, MM, SS)
file_to_edit = "auto_commit_bot.py"  # File to modify (can be this script or another file)
commit_message_prefix = "Auto-commit for"  # Message prefix

# === SCRIPT LOGIC ===
for i in range(num_commits):
    commit_date = start_date + timedelta(days=i)
    date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Make a change to the file (append a comment)
    with open(file_to_edit, 'a') as f:
        f.write(f"# {commit_message_prefix} {date_str}\n")

    # Stage the change
    subprocess.run(['git', 'add', file_to_edit])

    # Set environment variables for commit date
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str

    # Commit with the custom date
    subprocess.run([
        'git', 'commit', '-m', f'{commit_message_prefix} {date_str}'
    ], env=env)

# Push all commits
subprocess.run(['git', 'push'])

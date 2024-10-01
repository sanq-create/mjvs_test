from github import Github

# Replace with your details
access_token = "YOUR_PERSONAL_ACCESS_TOKEN"
repo_name = "username.github.io"  # Replace with your repo name
file_path = "path/to/your/file.txt"  # Replace with the path to your file
commit_message = "Add new file"

# Authenticate with GitHub
g = Github(access_token)

# Get the repository
repo = g.get_user().get_repo(repo_name)

# Read the content of the file
with open(file_path, 'rb') as file:
    content = file.read()

# Upload the file
repo.create_file("file.txt", commit_message, content)  # Adjust the target file name as needed
print("File uploaded successfully!")
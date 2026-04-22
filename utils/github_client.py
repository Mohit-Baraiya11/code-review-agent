import os
from github import Github,Auth
from dotenv import load_dotenv


load_dotenv()

SUPPORTED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".html", ".css", ".java", ".go", ".rs",
    ".cpp", ".c", ".h", ".rb", ".php"
}
MAX_FILE_SIZE = 100_0000  # skip files larger than 10MB

def get_github_client():
    token = os.getenv("GITHUB_TOKEN")
    auth = Auth.Token(token)
    return Github(auth=auth)

def fetch_repo_files(repo_url:str)->dict[str,str]:
    """
    Takes a GitHub repo URL, returns a dict of filename -> raw code content
    """
    client = get_github_client()
    # Extract owner/repo from URL
    # e.g. https://github.com/mohit/my-project -> mohit/my-project
    parts = repo_url.rstrip("/").split("github.com/")[-1]
    repo = client.get_repo(parts)
    files = {}
    contents = repo.get_contents("")

    while contents:
        file = contents.pop(0)
        if file.type == "dir":
            contents.extend(repo.get_contents(file.path))
        else:
            ext = os.path.splitext(file.name)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                if file.size <= MAX_FILE_SIZE:
                    try:
                        files[file.path] = file.decoded_content.decode("utf-8")
                    except Exception:
                        pass
    return files

result = fetch_repo_files("https://github.com/Mohit-Baraiya11/heart_disease")
print(list(result.keys()))  
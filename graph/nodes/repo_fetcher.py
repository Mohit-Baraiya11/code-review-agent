from graph.state import GraphState
from utils.github_client import fetch_repo_files

def repo_fetcher(state:GraphState)->GraphState:
    """
    Node 1: Fetches all code files from the GitHub repo URL in state.
    """
    print(f"[repo_fetcher] Fetching repo: {state['repo_url']}")
    files = fetch_repo_files(state["repo_url"])
    print(f"[repo_fetcher] Found {len(files)} files")
    for path in list(files.keys())[:5]:  # preview first 5
        print(f"  - {path}")

    return {"files": files}
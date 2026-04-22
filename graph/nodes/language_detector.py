from graph.state import GraphState
EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".jsx": "JavaScript",
    ".tsx": "TypeScript",
    ".html": "HTML",
    ".css": "CSS",
    ".java": "Java",
    ".go": "Go",
    ".rs": "Rust",
    ".cpp": "C++",
    ".c": "C",
    ".rb": "Ruby",
    ".php": "PHP",
}

def language_detector(state: GraphState) -> dict:
    """
    Node 2: Detects the primary language of the repo
    by counting file extensions.
    """
    files = state["files"]
    language_count = {}
    for filepath in files.keys():
        ext = "." + filepath.split(".")[-1].lower()
        print(f"  {filepath} -> ext: {ext}")
        language = EXTENSION_TO_LANGUAGE.get(ext)
        if language:
            language_count[language] = language_count.get(language, 0) + 1

    if not language_count:
        detected = "Unknown"
    else:
        # pick the language with most files
        detected = max(language_count, key=language_count.get)

    print(f"[language_detector] Language counts: {language_count}")
    print(f"[language_detector] Primary language: {detected}")

    return {"detected_language": detected}    
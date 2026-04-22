import os
import json
from langchain_groq import ChatGroq
from graph.state import GraphState, FileReview
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def load_prompt(filename: str, language: str, code: str, filepath: str) -> str:
    prompt_path = os.path.join("prompts", filename)
    with open(prompt_path, "r") as f:
        template = f.read()
    return template.replace("{language}", language)\
                   .replace("{filename}", filepath)\
                   + f"\n\nCode:\n{code}"


def code_quality(state: GraphState) -> dict:
    """
    Parallel Node 3c: Checks code quality in all files
    """
    print("[code_quality] Starting quality analysis...")

    files = state["files"]
    detected_language = state["detected_language"]
    file_reviews = []

    for filepath, code in files.items():
        ext = "." + filepath.split(".")[-1].lower()
        lang_map = {
            ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
            ".html": "HTML", ".css": "CSS", ".java": "Java",
            ".go": "Go", ".rs": "Rust", ".cpp": "C++",
            ".c": "C", ".rb": "Ruby", ".php": "PHP"
        }
        language = lang_map.get(ext, detected_language)

        prompt = load_prompt("quality.txt", language, code, filepath)

        try:
            response = llm.invoke(prompt)
            findings = json.loads(response.content)
        except Exception as e:
            print(f"  [code_quality] Error on {filepath}: {e}")
            findings = []

        if findings:
            print(f"  [code_quality] {filepath}: {len(findings)} issues found")
            file_reviews.append(FileReview(
                filename=filepath,
                language=language,
                findings=findings
            ))

    return {"file_reviews": file_reviews}
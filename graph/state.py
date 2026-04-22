from typing import TypedDict,Annotated
import operator

class FileReview(TypedDict):
    filename: str
    language: str
    findings: list[dict]

class GraphState(TypedDict):
    repo_url: str#
    focus: str  # "bugs" | "security" | "quality" | "all"
    files: dict[str, str]  # filename -> raw code content
    detected_language: str#
    file_reviews: Annotated[list[FileReview], operator.add]  # parallel agents write here
    critical_found: bool
    research_results: str
    final_report: str
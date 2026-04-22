import os
from langchain_groq import ChatGroq
from graph.state import GraphState
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def report_generator(state: GraphState) -> dict:
    """
    Node 6: Generates the final structured markdown report
    """
    print("[report_generator] Generating final report...")

    file_reviews = state["file_reviews"]
    research_results = state.get("research_results", "")
    repo_url = state.get("repo_url", "unknown")
    focus = state.get("focus", "all")
    detected_language = state.get("detected_language", "unknown")

    # build findings summary for prompt
    findings_text = ""
    for review in file_reviews:
        if review["findings"]:
            findings_text += f"\n### {review['filename']} ({review['language']})\n"
            for f in review["findings"]:
                severity = f.get("severity", "low").upper()
                msg = f.get("message", "")
                line = f.get("line", "?")
                ftype = f.get("type", "")
                findings_text += f"- [{severity}] ({ftype}) Line {line}: {msg}\n"

    research_text = ""
    if research_results:
        research_text = f"\n## Research Results\n{research_results}"

    prompt = f"""
        You are a senior software engineer writing a concise, honest code review report.

        Repository: {repo_url}
        Primary Language: {detected_language}
        Review Focus: {focus}

        Here are all the findings from the analysis:
        {findings_text}

        {research_text}

        IMPORTANT RULES:
        - Be proportional — if findings are minor, say so clearly
        - Do NOT inflate small issues into big problems
        - If a finding is a style preference or very minor, label it as such and keep it brief
        - Only dedicate serious attention to HIGH and CRITICAL issues
        - LOW and MEDIUM issues should be listed briefly in 1 line each, no long explanations
        - If the overall code quality is good, say that clearly in the summary
        - Do NOT repeat the same issue multiple times
        - Keep the entire report concise and honest

        Write a professional markdown report with these sections:
        1. ## Executive Summary - honest 2-3 sentence overall assessment
        2. ## Critical & High Issues - only if they exist, else skip this section
        3. ## Minor Issues - one line each, no drama
        4. ## Verdict - one sentence final verdict

        Be direct, proportional, and professional.
        """

    try:
        response = llm.invoke(prompt)
        final_report = response.content
    except Exception as e:
        print(f"[report_generator] Error: {e}")
        final_report = f"# Code Review Report\n\nError generating report: {e}"

    print("[report_generator] Report generated successfully!")
    return {"final_report": final_report}
import os
from tavily import TavilyClient
from graph.state import GraphState
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def deep_dive(state: GraphState) -> dict:
    """
    Optional Node 5: If critical issues found, search web
    for fix patterns and solutions using Tavily.
    """
    print("[deep_dive] Searching for fix patterns...")

    file_reviews = state["file_reviews"]
    research_results = []

    # collect only critical findings
    critical_findings = []
    for review in file_reviews:
        for finding in review["findings"]:
            if finding.get("severity", "").lower() == "critical":
                critical_findings.append({
                    "file": review["filename"],
                    "language": review["language"],
                    "message": finding["message"]
                })

    # search Tavily for each critical finding
    for finding in critical_findings[:3]:  # limit to 3 searches
        query = f"{finding['language']} {finding['message']} fix best practice"
        print(f"  [deep_dive] Searching: {query}")

        try:
            response = client.search(query, max_results=2)
            for result in response["results"]:
                research_results.append(
                    f"Issue: {finding['message']}\n"
                    f"Source: {result['url']}\n"
                    f"Summary: {result['content'][:300]}\n"
                )
        except Exception as e:
            print(f"  [deep_dive] Search error: {e}")

    combined = "\n---\n".join(research_results)
    print(f"[deep_dive] Found {len(research_results)} research results")

    return {"research_results": combined}
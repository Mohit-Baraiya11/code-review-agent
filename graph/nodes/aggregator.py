from graph.state import GraphState


SEVERITY_RANK = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3
}


def aggregator(state: GraphState) -> dict:
    """
    Node 4: Merges all findings from parallel agents,
    ranks by severity, checks if critical issues exist.
    """
    print("[aggregator] Aggregating all findings...")

    file_reviews = state["file_reviews"]
    critical_found = False
    total_findings = 0

    for review in file_reviews:
        for finding in review["findings"]:
            total_findings += 1
            if finding.get("severity") == "critical":
                critical_found = True

    # sort file_reviews by highest severity finding in each file
    def get_min_severity(review):
        if not review["findings"]:
            return 999
        return min(
            SEVERITY_RANK.get(f.get("severity", "low"), 3)
            for f in review["findings"]
        )

    sorted_reviews = sorted(file_reviews, key=get_min_severity)

    print(f"[aggregator] Total findings: {total_findings}")
    print(f"[aggregator] Critical issues found: {critical_found}")

    return {
        "file_reviews": sorted_reviews,
        "critical_found": critical_found
    }
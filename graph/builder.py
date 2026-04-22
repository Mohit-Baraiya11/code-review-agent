from langgraph.graph import StateGraph, END
from langgraph.types import Send
from graph.state import GraphState
from graph.nodes.repo_fetcher import repo_fetcher
from graph.nodes.language_detector import language_detector
from graph.nodes.bug_finder import bug_finder
from graph.nodes.security_analyzer import security_analyzer
from graph.nodes.code_quality import code_quality
from graph.nodes.aggregator import aggregator
from graph.nodes.deep_dive import deep_dive
from graph.nodes.report_generator import report_generator

def route_by_language(state: GraphState):
    language = state["detected_language"]
    print(f"[router_1] Routing for language: {language}")
    return [
        Send("bug_finder", state),
        Send("security_analyzer", state),
        Send("code_quality", state),
    ]
def route_by_severity(state: GraphState):
    if state["critical_found"]:
        print("[router_2] Critical issues found → deep dive")
        return "deep_dive"
    else:
        print("[router_2] No critical issues → report generator")
        return "report_generator"


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("repo_fetcher" , repo_fetcher)
    graph.add_node("language_detector", language_detector)
    graph.add_node("bug_finder", bug_finder)
    graph.add_node("security_analyzer", security_analyzer)
    graph.add_node("code_quality", code_quality)
    graph.add_node("aggregator", aggregator)
    graph.add_node("deep_dive", deep_dive)
    graph.add_node("report_generator", report_generator)

    # entry point
    graph.set_entry_point("repo_fetcher")

    graph.add_edge("repo_fetcher", "language_detector")

    graph.add_conditional_edges(
        "language_detector",
        route_by_language,
        ["bug_finder", "security_analyzer", "code_quality"]
    )
    graph.add_edge("bug_finder", "aggregator")
    graph.add_edge("security_analyzer", "aggregator")
    graph.add_edge("code_quality", "aggregator")

    graph.add_conditional_edges(
        "aggregator",
        route_by_severity,
        {
            "deep_dive": "deep_dive",
            "report_generator": "report_generator"
        }
    )
    graph.add_edge("deep_dive", "report_generator")

    # report generator → END
    graph.add_edge("report_generator", END)

    return graph.compile()

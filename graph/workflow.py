from langgraph.graph import StateGraph

from agents.planner_agent import planner
from agents.analyzer_agent import analyze
from agents.evaluator_agent import evaluate
from agents.optimizer_agent import optimize_resume
from agents.recommender_agent import recommend_jobs

def build_graph():

    graph = StateGraph(dict)

    graph.add_node("planner", planner)
    graph.add_node("analyzer", analyze)
    graph.add_node("evaluator", evaluate)
    graph.add_node("optimizer", optimize_resume)
    graph.add_node("recommender", recommend_jobs)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "analyzer")
    graph.add_edge("analyzer", "evaluator")
    graph.add_edge("evaluator", "optimizer")
    graph.add_edge("optimizer", "recommender")

    graph.set_finish_point("recommender")

    return graph.compile()
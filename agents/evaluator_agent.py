from utils.llm import get_llm, safe_invoke

llm = get_llm()

def evaluate(state):

    report = state["analysis"]

    prompt = f"""
    Evaluate the resume analysis.

    Improve the reasoning and identify mistakes.

    Report:
    {report}
    """

    result = safe_invoke(llm, prompt)

    state["evaluation"] = result.content

    return state
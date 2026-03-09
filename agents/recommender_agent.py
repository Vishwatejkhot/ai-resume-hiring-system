from utils.llm import get_llm, safe_invoke

llm = get_llm()

def recommend_jobs(state):

    report = state["evaluation"]

    prompt = f"""
    Based on the candidate evaluation suggest:

    1. Suitable job roles
    2. Skills to learn next
    """

    result = safe_invoke(llm, prompt)

    state["recommendations"] = result.content

    return state
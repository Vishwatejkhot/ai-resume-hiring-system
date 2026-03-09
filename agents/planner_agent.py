from utils.llm import get_llm, safe_invoke

llm = get_llm()

def planner(state):

    job = state["job_description"]

    prompt = f"""
    Create a plan to evaluate resumes for the job.

    Job description:
    {job}

    Provide analysis steps.
    """

    result = safe_invoke(llm, prompt)

    state["plan"] = result.content

    return state
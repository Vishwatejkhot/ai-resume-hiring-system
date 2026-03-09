from utils.llm import get_llm, safe_invoke

llm = get_llm()

def optimize_resume(state):

    job = state["job_description"]
    analysis = state["analysis"]

    prompt = f"""
    Rewrite the resume so it better matches the job description.

    Job Description:
    {job}

    Resume Analysis:
    {analysis}

    Produce an optimized resume with strong bullet points.
    """

    result = safe_invoke(llm, prompt)

    state["optimized_resume"] = result.content

    return state
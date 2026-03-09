from rag.retriever import retrieve
from utils.llm import get_llm, safe_invoke

llm = get_llm()

def analyze(state):

    job = state["job_description"]

    context = retrieve(job)

    prompt = f"""
    Analyze the resumes for this job.

    Job Description:
    {job}

    Resume Context:
    {context}

    Extract:
    - Matching skills
    - Missing skills
    - Experience summary
    """

    result = safe_invoke(llm, prompt)

    state["analysis"] = result.content

    return state
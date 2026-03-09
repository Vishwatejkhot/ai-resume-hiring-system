from rag.vector_store import load_db

def retrieve(query):

    db = load_db()

    docs = db.similarity_search(query, k=2)

    context = ""

    for d in docs:

        context += d.page_content + "\n"

    return context
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
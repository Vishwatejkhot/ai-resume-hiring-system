import os
from langchain_community.vectorstores.faiss import FAISS
from utils.embeddings import get_embeddings


VECTOR_PATH = "vector_db"

embeddings = get_embeddings()


def load_db():

    # if DB folder doesn't exist
    if not os.path.exists(VECTOR_PATH):
        return None

    try:
        db = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        return db

    except Exception:
        return None


def save_db(db):

    if not os.path.exists(VECTOR_PATH):
        os.makedirs(VECTOR_PATH)

    db.save_local(VECTOR_PATH)
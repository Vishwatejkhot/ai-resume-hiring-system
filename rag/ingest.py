from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from rag.vector_store import load_db, save_db
from utils.embeddings import get_embeddings
from langchain_community.vectorstores.faiss import FAISS
import uuid

embeddings = get_embeddings()

def ingest_resume(text, source):

    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,   
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

   
    docs = [
        Document(
            page_content=c,
            metadata={
                "candidate": source,
                "id": str(uuid.uuid4())
            }
        )
        for c in chunks
    ]

    
    db = load_db()

    
    if db is None:

        db = FAISS.from_documents(
            docs,
            embeddings
        )

  
    else:

        db.add_documents(docs)

    
    save_db(db)

    return db
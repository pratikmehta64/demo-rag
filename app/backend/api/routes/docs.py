from fastapi import APIRouter
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.schema import Document
from app.settings.models import embed_model, llm_model
from app.settings.constants import INDEX_DIR, DATA_DIR
from typing import Any

router = APIRouter(prefix="/docs", tags=["docs"])

@router.post("/")
def index_documents(
) -> dict[str, str]:
    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    if documents:
        index = VectorStoreIndex.from_documents(
            documents=documents,
            embed_model=embed_model,
        )
        # Save the index to the storage context
        index.storage_context.persist(INDEX_DIR)
        return {"message": "Documents indexed successfully."}
    else:
        return {"error": "No files provided for indexing."} 
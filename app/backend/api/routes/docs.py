from fastapi import APIRouter
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.schema import Document
from app.settings.models import embed_model
from app.settings.constants import INDEX_DIR
from typing import Any

router = APIRouter(prefix="/docs", tags=["docs"])

@router.post("/")
async def index_documents(
    *, 
    files: list[Document] = None,
) -> dict[str, str]:
    if files:
        index = VectorStoreIndex.from_documents(
            documents=files,
            embed_model=embed_model,
        )
        # Save the index to the storage context
        index.storage_context.persist(INDEX_DIR)
        return {"message": "Documents indexed successfully."}
    else:
        return {"error": "No files provided for indexing."} 
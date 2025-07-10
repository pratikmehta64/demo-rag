from fastapi import APIRouter
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.schema import Document
from app.settings.constants import INDEX_DIR
from app.settings.models import llm_model, embed_model
from app.backend.prompts.system_prompt import SystemPrompt

router = APIRouter(prefix="/llms", tags=["llms"])

@router.post("/")
def get_llm_response(
    *,
    user_query: str = None,
    length: str = "short",
):
    """
    Endpoint to get a response from the LLM model.
    """
    if not user_query:
        return {"error": "User query is required."}
    # Load the index from the storage context
    try:
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        index = load_index_from_storage(
            storage_context,
            embed_model=embed_model,
        )
        print("Index loaded successfully.")
        # if index:
            # Set and use the query engine with the provided index
        # sys_prompt = SystemPrompt()
        # if length.lower() == "short":
        #     sys_prompt.set_short_response_prompt()    
        # elif length.lower() == "long":
        #     sys_prompt.set_long_response_prompt()
        # else:
        #     return {"error": "Invalid length specified. Use 'short' or 'long'."}
        
        # llm_model.system_prompt = sys_prompt.get_prompt()
        query_engine = index.as_query_engine()
    except Exception as e:
        return {"error": f"Failed to load index or query engine: {str(e)}"}
    try:
        response = query_engine.query(user_query)
    except Exception as e:
        return {"error": f"Failed to query the LLM model: {str(e)}"}
    
    return {"response": response.response}




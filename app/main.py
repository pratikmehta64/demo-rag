from app.backend.api.routes.llms import router as llm_router
from app.backend.api.routes.docs import router as docs_router
from fastapi import FastAPI

app = FastAPI()

# Include the routers for LLM and document routes
app.include_router(llm_router)
app.include_router(docs_router)


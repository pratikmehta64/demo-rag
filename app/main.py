from app.backend.api.routes.llms import router as llm_router
from app.backend.api.routes.docs import router as docs_router
from fastapi import FastAPI

appl = FastAPI()

# Include the routers for LLM and document routes
appl.include_router(llm_router)
appl.include_router(docs_router)


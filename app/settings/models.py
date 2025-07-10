import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
from app.backend.prompts.system_prompt import SystemPrompt
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from app.settings.constants import LLM_MODEL_NAME, EMBED_MODEL_NAME

system_prompt = SystemPrompt()
# Create an agent workflow with the specified LLM model
# embed_model = Ollama(model=EMBED_MODEL_NAME)
embed_model = HuggingFaceEmbedding(model_name="all-mpnet-base-v2")

llm_model = Ollama(model=LLM_MODEL_NAME,
    request_timeout=360.0,
    system_prompt = system_prompt.get_prompt()
    )


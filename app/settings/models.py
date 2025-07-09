import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
from app.backend.prompts.system_prompt import SystemPrompt

from app.settings.constants import LLM_MODEL_NAME, EMBED_MODEL_NAME

system_prompt = SystemPrompt()
# Create an agent workflow with the specified LLM model
llm_model = FunctionAgent(
    llm=Ollama(model=LLM_MODEL_NAME),
    embed_model=EMBED_MODEL_NAME,
    request_timeout=360.0,
    system_prompt = system_prompt.get_prompt(),
)

embed_model = Ollama(model=EMBED_MODEL_NAME)
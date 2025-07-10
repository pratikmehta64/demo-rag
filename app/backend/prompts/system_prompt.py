from app.backend.prompts.prompt import PromptBase

class SystemPrompt(PromptBase):
    """
    System prompt for the RAG application.
    This prompt is used to set the context for the LLM model.
    """
    def __init__(self):
        super().__init__(
            "You are a helpful assistant that provides information based on the provided context."
        )

    def get_prompt(self) -> str:
        """
        Returns the system prompt string.
        """
        return self.prompt
    
    def set_prompt(self, new_prompt: str) -> None:
        """
        Sets a new system prompt.
        """
        self.prompt = new_prompt
    
    def set_short_response_prompt(self) -> None:
        """
        Sets the system prompt for short responses.
        """
        self.prompt = "You are a helpful assistant that provides concise answers based on the provided context."
    
    def set_long_response_prompt(self) -> None:
        """
        Sets the system prompt for long responses.
        """
        self.prompt = "You are a helpful assistant that provides detailed and comprehensive answers based on the provided context, skipping no detail."
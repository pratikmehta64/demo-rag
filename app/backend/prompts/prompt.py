class PromptBase:
    """
    Base class for prompts
    """
    def __init__(self, prompt: str):
        self.prompt = prompt

    def get_prompt(self) -> str:
        """
        Returns the prompt string
        """
        return self.prompt

    def __str__(self) -> str:
        return self.get_prompt()
from meta_ai_api import MetaAI

class AIAssistant:
    def __init__(self):
        self.ai = MetaAI()
        self.conversation_history = []  # Track conversation history

    def message(self, prompt, new_conversation=False):
        """
        Sends a message to the AI and returns the response.
        Handles conversation history and new conversations.
        """
        if new_conversation:
            self.conversation_history = []
        response = self.ai.prompt(message=prompt)
        self.conversation_history.append({"prompt": prompt, "response": response})
        return response

    def get_weather(self, location):
        """
        Queries the AI for weather information in a specific location.
        """
        prompt = f"What is the weather in {location} today?"
        return self.message(prompt)

    def get_sources(self, response):
        """
        Extracts source links from the AI response, if available.
        """
        sources = response.get("sources", [])
        if sources:
            return [source["link"] for source in sources]
        return None

    def get_image(self, prompt):
        """
        Generates an image based on a prompt.
        """
        response = self.ai.prompt(message=prompt)
        return response.get("media", [])

    def follow_conversation(self, prompt):
        """
        Sends a message related to the conversation history.
        """
        return self.message(prompt)

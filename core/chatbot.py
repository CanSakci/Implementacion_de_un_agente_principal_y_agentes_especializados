"""Lógica principal del chatbot: ejecuta el agente principal y muestra el resultado."""

from agents import Runner
from core.conversation import Conversation
from post_agents.main_agent import main_agent
from post_agents.specialized_agents import LinkedinPost


class Chatbot:
    """Chatbot de terminal sobre el OpenAI Agents SDK."""

    def __init__(self) -> None:
        self.conversation = Conversation()

    def ask(self, user_text: str) -> None:
        """Ejecuta un turno completo del chatbot."""
        input_data = self.conversation.input_for(user_text)
        result = Runner.run_sync(main_agent, input_data)
        self.conversation.update(result)

        active_agent_name = result.last_agent.name
        print(f"\n[🤖 Agente Activo: {active_agent_name}]")

        if isinstance(result.final_output, LinkedinPost):
            self._mostrar_post(result.final_output)
        else:
            print(f"\n{result.final_output}\n")

    @staticmethod
    def _mostrar_post(post: LinkedinPost) -> None:
        """Muestra los campos del post de LinkedIn de forma organizada y visual."""
        print("\n" + "★" * 60)
        print(f"  TÍTULO: {post.title}")
        print(f"  CATEGORÍA: [{post.category.upper()}]")
        print("★" * 60 + "\n")
        
        print(post.content)
        print("\n" + "-" * 60)
        
        formatted_hashtags = " ".join(
            f"#{tag.lstrip('#')}" for tag in post.hashtags
        )
        print(f"Hashtags: {formatted_hashtags}")
        print("=" * 60 + "\n")
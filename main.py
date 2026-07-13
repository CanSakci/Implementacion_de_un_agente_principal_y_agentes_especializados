"""Logica principal del chatbot: ejecuta el agente principal y muestra el resultado."""

from core.conversation import Conversation
from post_agents.main_agent import main_agent
from post_agents.specialized_agents import LinkedinPost


class Chatbot:
    """Chatbot de terminal sobre el OpenAI Agents SDK."""

    def __init__(self) -> None:
        self.conversation = Conversation()

    def ask(self, user_text: str) -> None:
        """Ejecuta un turno completo.

        TODO:
        1. Ejecuta el agente principal con Runner.run_sync(main_agent, entrada),
           donde la entrada es self.conversation.input_for(user_text).
        2. Actualiza el historial con self.conversation.update(result).
        3. Muestra el indicador del agente que ha respondido
           (result.last_agent.name).
        4. Si result.final_output es un LinkedinPost, muestralo con
           self._mostrar_post; si no, imprime el texto tal cual.
        """
        raise NotImplementedError("TODO: ejecuta el turno con Runner.run_sync")

    @staticmethod
    def _mostrar_post(post: LinkedinPost) -> None:
        """Muestra los campos del post de forma organizada.

        TODO: imprime title, category, content y hashtags de forma clara
        (por ejemplo con separadores y los hashtags precedidos de #).
        """
        raise NotImplementedError("TODO: muestra el post estructurado")

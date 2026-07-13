"""Gestión del historial de la conversación entre turnos."""


class Conversation:
    """Mantiene el historial en el formato de ítems del Agents SDK."""

    def __init__(self) -> None:
        self._items: list = []

    def input_for(self, user_text: str) -> list:
        """Historial previo + el nuevo mensaje del usuario, listo para el Runner."""
        return self._items + [{"role": "user", "content": user_text}]

    def update(self, result) -> None:
        """Guarda el estado devuelto por el Runner tras un turno."""
        self._items = result.to_input_list()
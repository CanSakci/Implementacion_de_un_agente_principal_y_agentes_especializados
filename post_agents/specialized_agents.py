"""Agentes especializados por temática y modelo Pydantic de la publicación."""

from agents import Agent
from pydantic import BaseModel, Field

MODEL = "gpt-4o-mini"


class LinkedinPost(BaseModel):
    """Estructura común de toda publicación generada para LinkedIn."""
    title: str = Field(description="Un titular atractivo y profesional para LinkedIn.")
    content: str = Field(description="El cuerpo principal del post, bien estructurado con párrafos claros.")
    hashtags: list[str] = Field(description="Lista de hashtags relevantes (sin el símbolo #, solo las palabras).")
    category: str = Field(description="La categoría o temática de la publicación (e.g., Marketing, Programación, Legal).")


marketing_agent = Agent(
    name="Agente de Marketing",
    instructions=(
        "Eres un experto estratega de contenidos para LinkedIn especializado en marketing digital, "
        "ventas, branding y crecimiento de negocio. Tu objetivo es redactar publicaciones persuasivas, "
        "atractivas y optimizadas para generar engagement. Debes devolver SIEMPRE tu respuesta "
        "ajustándote estrictamente al esquema estructurado de LinkedinPost."
    ),
    handoff_description="Útil para crear publicaciones sobre marketing digital, estrategias de ventas, branding, redes sociales o marca personal.",
    model=MODEL,
    output_type=LinkedinPost,
)

programacion_agent = Agent(
    name="Agente de Programación",
    instructions=(
        "Eres un ingeniero de software senior y divulgador tecnológico en LinkedIn. Escribes publicaciones "
        "sobre desarrollo de software, buenas prácticas de código, arquitectura, inteligencia artificial, "
        "frameworks modernos y resolución de problemas técnicos. Tu tono es informativo, preciso y accesible. "
        "Debes devolver SIEMPRE tu respuesta ajustándote estrictamente al esquema estructurado de LinkedinPost."
    ),
    handoff_description="Útil para generar publicaciones sobre desarrollo de software, programación, inteligencia artificial, tecnología y arquitectura de sistemas.",
    model=MODEL,
    output_type=LinkedinPost,
)

juridico_agent = Agent(
    name="Agente Jurídico-Legal",
    instructions=(
        "Eres un abogado corporativo y consultor legal especializado en derecho tecnológico, cumplimiento "
        "normativo (compliance), propiedad intelectual, RGPD y regulación empresarial. Escribes contenido "
        "profesional, riguroso y claro para LinkedIn, explicando conceptos legales complejos de forma comprensible "
        "para directivos y empresas. Debes devolver SIEMPRE tu respuesta ajustándote estrictamente al esquema de LinkedinPost."
    ),
    handoff_description="Útil para redactar publicaciones sobre leyes, regulación, compliance, derecho laboral, propiedad intelectual o normas tecnológicas (e.g., IA Act, RGPD).",
    model=MODEL,
    output_type=LinkedinPost,
)

SPECIALIZED_AGENTS = [a for a in (marketing_agent, programacion_agent, juridico_agent) if a]
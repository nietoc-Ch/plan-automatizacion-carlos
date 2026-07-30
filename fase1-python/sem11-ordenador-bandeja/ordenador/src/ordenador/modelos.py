from dataclasses import dataclass
from enum import Enum


class Etiqueta(str, Enum):
    """
    Enum que representa las etiquetas posibles para un email.
    Serializable como string.
    """

    URGENTE = "urgente"
    FACTURA = "factura"
    SPAM = "spam"
    PERSONAL = "personal"
    TRABAJO = "trabajo"


@dataclass
class Email:
    """
    Modelo de datos para un email.

    Atributos:
        remitente: Dirección de correo del remitente.
        asunto: Asunto del email.
        fecha: Fecha del email (en formato ISO 8601).
        cuerpo: Contenido del email.
        etiqueta: Etiqueta asociada al email.
    """

    remitente: str
    asunto: str
    fecha: str
    cuerpo: str
    etiqueta: Etiqueta = Etiqueta.TRABAJO

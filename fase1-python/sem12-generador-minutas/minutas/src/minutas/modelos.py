from dataclasses import asdict, dataclass, field


@dataclass
class Accion:
    """
    Representa una acción dentro de una minuta.

    Attributes:
        responsable (str): Nombre del responsable de la acción.
        tarea (str): Descripción de la tarea o acción a realizar.
        plazo (str | None): Fecha límite o plazo para la acción. Puede ser None si no se informa.
    """

    responsable: str
    tarea: str
    plazo: str | None = None

    def to_dict(self) -> dict:
        """
        Convierte la acción en un diccionario.

        Returns:
            dict: Representación de la acción como diccionario.
        """
        return asdict(self)

    def to_markdown(self) -> str:
        """
        Convierte la acción a una representación en Markdown.

        Returns:
            str: Representación en Markdown de la acción.
        """
        md = f"- **Responsable:** {self.responsable}\n  **Tarea:** {self.tarea}"
        if self.plazo:
            md += f"\n  **Plazo:** {self.plazo}"
        return md


@dataclass
class Minuta:
    """
    Representa una minuta procesada.

    Attributes:
        titulo (str): Título de la minuta.
        fecha (str): Fecha de la minuta en formato ISO.
        participantes (list[str]): Lista de participantes.
        resumen (str): Resumen de la minuta.
        acciones (list[Accion]): Lista de acciones incluidas en la minuta.
    """

    titulo: str
    fecha: str
    participantes: list[str]
    resumen: str
    acciones: list[Accion] = field(default_factory=list)

    def to_dict(self) -> dict:
        """
        Convierte la minuta en un diccionario.

        Returns:
            dict: Representación de la minuta como diccionario.
        """
        return {
            "titulo": self.titulo,
            "fecha": self.fecha,
            "participantes": self.participantes,
            "resumen": self.resumen,
            "acciones": [accion.to_dict() for accion in self.acciones],
        }

    def to_markdown(self) -> str:
        """
        Convierte la minuta en una representación en Markdown.

        Returns:
            str: Representación en Markdown de la minuta.
        """
        participantes_md = ", ".join(self.participantes)
        acciones_md = "\n\n".join(accion.to_markdown() for accion in self.acciones)
        md = (
            f"# {self.titulo}\n"
            f"**Fecha:** {self.fecha}\n"
            f"**Participantes:** {participantes_md}\n\n"
            f"## Resumen\n"
            f"{self.resumen}\n\n"
            f"## Acciones\n"
            f"{acciones_md if acciones_md else 'No hay acciones registradas.'}"
        )
        return md

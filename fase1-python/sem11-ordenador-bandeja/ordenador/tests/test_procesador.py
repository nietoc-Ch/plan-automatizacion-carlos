from pathlib import Path

import pytest

from ordenador.modelos import Email, Etiqueta
from ordenador.procesador import (
    calcular_estadisticas,
    clasificar_todos,
    leer_emails,
)


def test_calcular_estadisticas_basico() -> None:
    emails = [
        Email(
            "a@a.com",
            "Asunto urgente",
            "2024-02-01",
            "Cuerpo urgente",
            Etiqueta.URGENTE,
        ),
        Email(
            "b@b.com", "Factura adjunta", "2024-02-02", "Ver factura", Etiqueta.FACTURA
        ),
        Email(
            "c@gmail.com",
            "¿Vamos a cenar?",
            "2024-02-03",
            "Invitación",
            Etiqueta.PERSONAL,
        ),
        Email(
            "d@b.com",
            "Asunto urgente",
            "2024-02-04",
            "Más urgente todavía",
            Etiqueta.URGENTE,
        ),
    ]
    stats = calcular_estadisticas(emails)
    assert stats == {
        "urgente": 2,
        "factura": 1,
        "personal": 1,
    }


def test_leer_emails_file_not_found() -> None:
    ruta = Path("no_existe_este_archivo_123456.csv")
    with pytest.raises(FileNotFoundError):
        leer_emails(ruta)


def test_clasificar_todos_no_mutacion() -> None:
    emails = [
        Email("uno@uno.com", "Asunto 1", "2024-02-01", "Texto 1"),
        Email("amigo@gmail.com", "Hola", "2024-02-02", "¿Cómo estás?"),
    ]
    emails_original = [
        Email(e.remitente, e.asunto, e.fecha, e.cuerpo, e.etiqueta) for e in emails
    ]
    resultado = clasificar_todos(emails)

    # Verifica que emails_original siguen con la etiqueta por defecto (TRABAJO)
    for original, despues in zip(emails_original, emails):
        assert despues.etiqueta == original.etiqueta == Etiqueta.TRABAJO

    # El resultado tiene etiquetas clasificadas correctamente
    etiquetas_esperadas = [
        Etiqueta.TRABAJO,
        Etiqueta.PERSONAL,
    ]
    reales = [email.etiqueta for email in resultado]
    assert reales == etiquetas_esperadas

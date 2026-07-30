import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from ordenador.modelos import Email
from ordenador.reglas import clasificar_email


def leer_emails(ruta: Path) -> list[Email]:
    """
    Lee un archivo CSV de emails y devuelve una lista de instancias Email.

    Args:
        ruta: Ruta al archivo CSV con columnas remitente, asunto, fecha y cuerpo.

    Returns:
        Lista de emails leídos del CSV.

    Raises:
        FileNotFoundError: Si el archivo no existe.
    """
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {ruta}")

    emails: list[Email] = []
    with ruta.open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            emails.append(
                Email(
                    remitente=fila["remitente"],
                    asunto=fila["asunto"],
                    fecha=fila["fecha"],
                    cuerpo=fila["cuerpo"],
                )
            )
    return emails


def clasificar_todos(emails: list[Email]) -> list[Email]:
    """
    Clasifica cada email y devuelve una nueva lista con las etiquetas calculadas.

    Función pura: no modifica la lista de entrada.

    Args:
        emails: Lista de emails sin clasificar o con etiquetas previas.

    Returns:
        Nueva lista de emails con la etiqueta asignada por las reglas.
    """
    return [
        Email(
            remitente=email.remitente,
            asunto=email.asunto,
            fecha=email.fecha,
            cuerpo=email.cuerpo,
            etiqueta=clasificar_email(email),
        )
        for email in emails
    ]


def escribir_csv(emails: list[Email], ruta: Path) -> None:
    """
    Escribe una lista de emails clasificados en un archivo CSV.

    Args:
        emails: Lista de emails con etiqueta asignada.
        ruta: Ruta del archivo CSV de salida.
    """
    campos = ["remitente", "asunto", "fecha", "cuerpo", "etiqueta"]
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for email in emails:
            escritor.writerow(
                {
                    "remitente": email.remitente,
                    "asunto": email.asunto,
                    "fecha": email.fecha,
                    "cuerpo": email.cuerpo,
                    "etiqueta": email.etiqueta.value,
                }
            )


def calcular_estadisticas(emails: list[Email]) -> dict[str, int]:
    """
    Calcula la frecuencia de cada etiqueta en la lista de emails.

    Args:
        emails: Lista de emails clasificados.

    Returns:
        Diccionario con la cantidad de emails por etiqueta.
    """
    contador = Counter(email.etiqueta.value for email in emails)
    return dict(contador)


def escribir_estadisticas(stats: dict[str, int], ruta: Path) -> None:
    """
    Escribe las estadísticas de clasificación en un archivo JSON.

    Args:
        stats: Diccionario con la frecuencia por etiqueta.
        ruta: Ruta del archivo JSON de salida.
    """
    datos = {
        "generado_en": datetime.now().isoformat(),
        "total": sum(stats.values()),
        "por_etiqueta": stats,
    }
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
        archivo.write("\n")


def procesar_archivo(
    entrada: Path, salida_csv: Path, salida_json: Path
) -> dict[str, int]:
    """
    Orquesta la lectura, clasificación, escritura y generación de estadísticas.

    Args:
        entrada: Ruta al CSV de emails de entrada.
        salida_csv: Ruta al CSV de emails clasificados.
        salida_json: Ruta al JSON con estadísticas de clasificación.

    Returns:
        Diccionario con la frecuencia de cada etiqueta.
    """
    emails = leer_emails(entrada)
    emails_clasificados = clasificar_todos(emails)
    escribir_csv(emails_clasificados, salida_csv)
    stats = calcular_estadisticas(emails_clasificados)
    escribir_estadisticas(stats, salida_json)
    return stats

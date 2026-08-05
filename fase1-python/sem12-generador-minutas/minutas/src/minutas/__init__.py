import argparse
import json
import sys
from pathlib import Path

from .extractor import extraer_minuta


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Procesa las notas de una reunión y extrae la minuta en Markdown y JSON."
    )
    parser.add_argument(
        "entrada",
        type=Path,
        help="Archivo de entrada con la transcripción de la reunión (texto plano)",
    )
    parser.add_argument(
        "--salida-md",
        type=Path,
        default=Path("minuta.md"),
        help="Ruta del archivo de salida en formato Markdown (por defecto: minuta.md)",
    )
    parser.add_argument(
        "--salida-json",
        type=Path,
        default=Path("minuta.json"),
        help="Ruta del archivo de salida en formato JSON (por defecto: minuta.json)",
    )

    args = parser.parse_args()

    try:
        texto = args.entrada.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {args.entrada}", file=sys.stderr)
        sys.exit(1)

    minuta = extraer_minuta(texto)

    # Guardar Markdown
    try:
        args.salida_md.write_text(minuta.to_markdown(), encoding="utf-8")
    except Exception as e:
        print(f"Error escribiendo el archivo Markdown: {e}", file=sys.stderr)
        sys.exit(1)

    # Guardar JSON
    try:
        args.salida_json.write_text(
            json.dumps(minuta.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as e:
        print(f"Error escribiendo el archivo JSON: {e}", file=sys.stderr)
        sys.exit(1)

    print("Resumen de la minuta procesada:")
    print(f"  Título: {minuta.titulo}")
    print(f"  Fecha: {minuta.fecha}")
    print(f"  Participantes: {len(minuta.participantes)}")
    print(f"  Acciones encontradas: {len(minuta.acciones)}")
    print(f"  Archivo Markdown: {args.salida_md.resolve()}")
    print(f"  Archivo JSON: {args.salida_json.resolve()}")

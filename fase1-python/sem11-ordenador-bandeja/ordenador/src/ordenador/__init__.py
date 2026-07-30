"""Ordenador de bandeja: CLI para clasificar emails."""

import argparse
import sys
from pathlib import Path

from ordenador.procesador import procesar_archivo


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clasifica emails en un CSV y genera estadísticas."
    )
    parser.add_argument(
        "entrada",
        type=Path,
        help="Archivo CSV de emails a procesar",
    )
    parser.add_argument(
        "--salida-csv",
        type=Path,
        default=Path("emails_clasificados.csv"),
        help="Ruta para el CSV con los emails clasificados",
    )
    parser.add_argument(
        "--salida-json",
        type=Path,
        default=Path("estadisticas.json"),
        help="Ruta para el JSON con las estadísticas",
    )
    args = parser.parse_args()

    try:
        estadisticas = procesar_archivo(args.entrada, args.salida_csv, args.salida_json)
    except FileNotFoundError as e:
        print(f"[ERROR] Archivo no encontrado: {e}", file=sys.stderr)
        sys.exit(1)

    ancho = max((len(str(etiqueta)) for etiqueta in estadisticas.keys()), default=8)
    print("Estadísticas:")
    total = 0
    for etiqueta, cantidad in estadisticas.items():
        print(f"  {str(etiqueta).ljust(ancho)} : {cantidad}")
        total += cantidad
    print(f"  {'TOTAL'.ljust(ancho)} : {total}")
    print()
    print(f"Archivo de emails clasificados: {args.salida_csv}")
    print(f"Archivo de estadísticas JSON : {args.salida_json}")

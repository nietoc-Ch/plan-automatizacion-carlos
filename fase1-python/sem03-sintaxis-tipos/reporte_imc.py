"""Generador de reporte IMC.

Integra pathlib + datetime + json + imc_lib en un pipeline real.
Es el patrón de cualquier automatización: leer → procesar → escribir.
"""

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from imc_lib import Persona, calcular_persona


def cargar_personas(ruta: Path) -> list[Persona]:
    """Lee un archivo JSON con la lista de personas y devuelve list[Persona]."""
    if not ruta.exists():
        raise FileNotFoundError(f"No existe: {ruta}")
    datos = json.loads(ruta.read_text())
    return [Persona(**p) for p in datos]


def calcular_reporte(personas: list[Persona]) -> dict:
    """Procesa la lista de Persona y devuelve un reporte con resultados + estadísticas."""
    resultados = []
    for p in personas:
        persona_calc = calcular_persona(p)
        resultados.append(asdict(persona_calc))

    imcs = [r["imc"] for r in resultados]
    return {
        "generado_en": datetime.now().isoformat(timespec="seconds"),
        "n_personas": len(resultados),
        "imc_promedio": round(sum(imcs) / len(imcs), 2) if imcs else 0,
        "imc_max": max(imcs) if imcs else 0,
        "imc_min": min(imcs) if imcs else 0,
        "personas": resultados,
    }


def guardar_reporte(reporte: dict, carpeta: Path) -> Path:
    """Guarda el reporte con timestamp en el nombre."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    ruta = carpeta / f"reporte_{timestamp}.json"
    ruta.write_text(json.dumps(reporte, indent=2, ensure_ascii=False))
    return ruta


def main():
    cwd = Path.cwd()
    fuente = cwd / "personas.json"

    print(f"Leyendo {fuente.name}...")
    personas = cargar_personas(fuente)
    print(f"  {len(personas)} personas cargadas")

    print("\nCalculando reporte...")
    reporte = calcular_reporte(personas)

    print(f"  IMC promedio: {reporte['imc_promedio']}")
    print(f"  Rango:        {reporte['imc_min']} - {reporte['imc_max']}")

    ruta = guardar_reporte(reporte, cwd)
    print(f"\nReporte guardado en {ruta.name}")


if __name__ == "__main__":
    main()

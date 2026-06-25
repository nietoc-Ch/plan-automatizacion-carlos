"""Generador de reporte IMC.

Integra pathlib + datetime + json + imc_lib en un pipeline real.
Es el patrón de cualquier automatización: leer → procesar → escribir.
"""

import json
from datetime import datetime
from pathlib import Path

from imc_lib import calcular_imc, clasificar_imc


def cargar_personas(ruta: Path) -> list[dict]:
    """Lee un archivo JSON con la lista de personas."""
    if not ruta.exists():
        raise FileNotFoundError(f"No existe: {ruta}")
    return json.loads(ruta.read_text())


def calcular_reporte(personas: list[dict]) -> dict:
    """Procesa la lista y devuelve un reporte con resultados + estadísticas."""
    resultados = []
    for p in personas:
        imc = calcular_imc(p["peso_kg"], p["altura_m"])
        resultados.append(
            {
                "nombre": p["nombre"],
                "peso_kg": p["peso_kg"],
                "altura_m": p["altura_m"],
                "imc": round(imc, 2),
                "categoria": clasificar_imc(imc),
            }
        )

    imcs = [r["imc"] for r in resultados]
    return {
        "generado_en": datetime.now().isoformat(timespec="seconds"),
        "n_personas": len(resultados),
        "imc_promedio": round(sum(imcs) / len(imcs), 2),
        "imc_max": max(imcs),
        "imc_min": min(imcs),
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

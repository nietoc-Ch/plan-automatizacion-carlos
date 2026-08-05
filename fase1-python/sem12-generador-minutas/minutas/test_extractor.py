"""Test rápido del extractor."""
from pathlib import Path
from minutas.extractor import extraer_minuta

texto = Path("minuta_ejemplo.txt").read_text()
minuta = extraer_minuta(texto)

print("TÍTULO:", minuta.titulo)
print("FECHA:", minuta.fecha)
print("PARTICIPANTES:", minuta.participantes)
print("ACCIONES:")
for a in minuta.acciones:
    print(f"  - {a.responsable}: {a.tarea!r} (plazo: {a.plazo!r})")
print("RESUMEN (primeros 200 chars):", minuta.resumen[:200])

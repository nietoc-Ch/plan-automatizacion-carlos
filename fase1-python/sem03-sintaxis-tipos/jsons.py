"""Demostración de json: serializar y deserializar dicts."""

import json
from pathlib import Path


def main():
    # ====== Diccionario Python ======
    persona = {
        "nombre": "Carlos",
        "edad": 44,
        "altura_m": 1.80,
        "es_dev": True,
        "hobbies": ["leer", "código", "viajar"],
        "direccion": {
            "calle": "Calle Mayor",
            "ciudad": "Madrid",
            "pais": "España",
        },
    }

    # ====== dict → JSON string ======
    # json.dumps (dump-string) → devuelve string
    json_compacto = json.dumps(persona)
    print("Compacto:")
    print(json_compacto)

    # indent=2 para formato legible
    json_bonito = json.dumps(persona, indent=2, ensure_ascii=False)
    print("\nBonito (legible):")
    print(json_bonito)

    # ensure_ascii=False respeta acentos y ñ.
    # Sin él, "España" se serializaría como "Espa\u00f1a".

    # ====== JSON string → dict ======
    # json.loads (load-string) → devuelve dict
    entrada = '{"nombre": "Ana", "edad": 30, "activa": true}'
    persona_ana = json.loads(entrada)
    print(f"\nParseado: {persona_ana}")
    print(f"Tipo:     {type(persona_ana).__name__}")
    print(f"Nombre:   {persona_ana['nombre']}")

    # ====== Manejo de errores ======
    json_roto = '{"esto": no es JSON válido}'
    try:
        json.loads(json_roto)
    except json.JSONDecodeError as e:
        print(f"\nError al parsear: {e.msg} en posición {e.pos}")

    # ====== Escribir/leer archivo JSON con pathlib ======
    ruta = Path.cwd() / "persona.json"

    # Forma 1: json.dumps + Path.write_text
    ruta.write_text(json.dumps(persona, indent=2, ensure_ascii=False))
    print(f"\nGuardado en {ruta.name}")

    # Leer de vuelta
    contenido = ruta.read_text()
    persona_leida = json.loads(contenido)
    print(f"Leído: {persona_leida['nombre']} tiene {persona_leida['edad']} años.")

    # Verificar que coincide con el original (round-trip)
    assert persona == persona_leida, "El round-trip falló"
    print("Round-trip exitoso: dict → JSON → archivo → JSON → dict idéntico.")

    # Limpiar
    ruta.unlink()


if __name__ == "__main__":
    main()

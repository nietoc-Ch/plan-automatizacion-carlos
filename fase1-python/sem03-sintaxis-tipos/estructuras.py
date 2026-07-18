"""Dicts, sets y tuples: las 3 estructuras de datos principales de Python."""

from collections import Counter
from typing import Any

# ===== DICTS =====

# Devuelve el valor de la key o el default si no existe (usa dict.get())


def valor_seguro(d: dict, key: str, default=None):
    return d.get(key, default)


# Cuenta la frecuencia de cada palabra en una lista. Devuelve dict[palabra, count]
def contar_palabras(lista: list[str]) -> dict[str, int]:
    return dict(Counter(lista))


# Devuelve un nuevo dict con solo las entradas cuyo valor supere min_valor
def filtrar_por_valor(d: dict[str, int], min_valor: int) -> dict[str, int]:
    return {k: v for k, v in d.items() if v > min_valor}


# Combi a dos dicts. Si hay colisión de keys, gana el segundo (usa | operator, Python 3.9+)
def combinar_dicts(a: dict, b: dict) -> dict:
    return a | b


# ===== SETS =====


# Devuelve una lista sin duplicados


def deduplicar(lista: list[Any]) -> list[Any]:
    return list(set(lista))


# Devuelve una las palabras que aparecen en ambas listas (intersección)


def palabras_comunes(a: list[str], b: list[str]) -> set[str]:
    return set(a) & set(b)


# Devuelve las palabras que aparece en 'a' pero NO en 'b' (diferencia)
def solo_en_a(a: list[str], b: list[str]) -> set[str]:
    return set(a) - set(b)


# ===== TUPLES =====


# Devuelve (media, minimo, maximo) de una lista de numeros
def estadisticas(lista: list[float]) -> tuple[float, float, float]:
    media = sum(lista) / len(lista)
    return (media, min(lista), max(lista))


def main():
    # ---- Dicts ----
    edades = {"Ana": 30, "Luis": 25, "Carlos": 44, "Eva": 28}

    print("=== DICTS ===")
    print(f"Edad de Ana:              {valor_seguro(edades, 'Ana', 0)}")
    print(f"Edad de 'Nadie' (default): {valor_seguro(edades, 'Nadie', 0)}")

    palabras = ["hola", "mundo", "hola", "python", "python", "python"]
    print(f"Frecuencias:              {contar_palabras(palabras)}")
    print(f"Mayores de 27:            {filtrar_por_valor(edades, 27)}")

    otros = {"Luis": 99, "Mario": 40}
    print(f"Combinado:                {combinar_dicts(edades, otros)}")

    # ---- Sets ----
    print("\n=== SETS ===")
    duplicados = [1, 2, 2, 3, 3, 3, 4]
    print(f"Sin duplicados:           {deduplicar(duplicados)}")

    lista_a = ["python", "java", "rust", "go"]
    lista_b = ["python", "javascript", "rust", "kotlin"]
    print(f"Comunes:                  {palabras_comunes(lista_a, lista_b)}")
    print(f"Solo en A:                {solo_en_a(lista_a, lista_b)}")

    # ---- Tuples ----
    print("\n=== TUPLES ===")
    nums = [4.5, 7.2, 1.8, 9.1, 5.5]
    media, mn, mx = estadisticas(nums)  # unpacking en 3 variables
    print(f"Media: {media:.2f}, Min: {mn}, Max: {mx}")


if __name__ == "__main__":
    main()

"""Control de flujo en Python: bucles, condicionales, comparaciones."""


def main():
    # ====== for con range ======
    # range(5) genera 0, 1, 2, 3, 4 — NO incluye el final
    # En Java: for (int i = 0; i < 5; i++)
    print("for i in range(5):")
    for i in range(5):
        print(f"  i = {i}")

    # range con inicio, fin y paso
    # range(2, 10, 2) → 2, 4, 6, 8
    print("\nrange(2, 10, 2):")
    for n in range(2, 10, 2):
        print(f"  n = {n}")

    # ====== for sobre una lista (foreach directo) ======
    # En Java: for (String idioma : idiomas)
    print("\nIdiomas:")
    idiomas = ["Python", "Java", "C++", "JavaScript"]
    for idioma in idiomas:
        print(f"  - {idioma}")

    # ====== while + break + continue ======
    # break sale del bucle; continue salta a la siguiente iteración
    print("\nPares hasta 20 (con continue):")
    n = 0
    while n < 20:
        n += 1
        if n % 2 != 0:    # si es impar, saltar
            continue
        print(f"  {n}", end=" ")
    print()

    # ====== Comparaciones encadenadas (esto NO existe en Java) ======
    print("\nComparaciones encadenadas:")
    x = 7
    if 0 < x < 10:
        print(f"  {x} está entre 0 y 10")
    else:
        print(f"  {x} no está entre 0 y 10")

    # ====== Operadores lógicos: and / or / not (no &&, ||, !) ======
    edad = 30
    tiene_carnet = True
    if edad >= 18 and tiene_carnet:
        print(f"  Puede conducir edad={edad}, carnet={tiene_carnet}")
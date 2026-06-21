"""Interfaz interactiva del IMC: pide datos al usuario y muestra resultado.

Importa la lógica pura de imc_lib. Esta capa solo hace I/O y orquestación.
"""

from imc_lib import calcular_imc, clasificar_imc


def main():
    print("=== Calculadora de IMC ===\n")

    nombre = input("¿Cómo te llamas? ")
    peso_str = input("Tu peso en kg (ej. 78.5): ")
    altura_str = input("Tu altura en metros (ej. 1.80): ")

    # Conversión: ValueError si el usuario escribe texto
    try:
        peso_kg = float(peso_str)
        altura_m = float(altura_str)
    except ValueError:
        print(f"\nError: '{peso_str}' o '{altura_str}' no son números válidos.")
        return

    # Cálculo: ValueError si los números no son positivos
    try:
        imc = calcular_imc(peso_kg, altura_m)
    except ValueError as e:
        print(f"\nError: {e}")
        return

    categoria = clasificar_imc(imc)

    print(f"\nHola {nombre}.")
    print(f"  IMC: {imc:.2f}")
    print(f"  Categoría: {categoria}")


if __name__ == "__main__":
    main()

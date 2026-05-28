"""Calculadora de IMC interactiva: pide datos al usuario y devuelve resultado."""


def main():
    print("=== Calculadora de IMC ===\n")

    # input() siempre devuelve string, incluso si escribes "44"
    nombre = input("¿Cómo te llamas? ")

    # Para convertir a número usamos float() o int()
    # Si el usuario escribe algo no convertible, lanza ValueError
    peso_str = input("Tu peso en kg (ej. 78.5): ")
    altura_str = input("Tu altura en metros (ej. 1.80): ")

    # Conversión con manejo de errores (try/except)
    try:
        peso_kg = float(peso_str)
        altura_m = float(altura_str)
    except ValueError:
        print(f"\nError: '{peso_str}' o '{altura_str}' no son números válidos.")
        return  # sale de la función sin hacer el resto

    # Validación lógica
    if peso_kg <= 0 or altura_m <= 0:
        print("\nError: peso y altura deben ser positivos.")
        return

    imc = peso_kg / (altura_m**2)

    if imc < 18.5:
        categoria = "bajo peso"
    elif imc < 25:
        categoria = "normal"
    elif imc < 30:
        categoria = "sobrepeso"
    else:
        categoria = "obesidad"

    print(f"\nHola {nombre}.")
    print(f"  IMC: {imc:.2f}")
    print(f"  Categoría: {categoria}")


if __name__ == "__main__":
    main()

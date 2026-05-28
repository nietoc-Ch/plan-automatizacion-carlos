"""Calcula el IMC (Índice de Masa Corporal)."""


def main():
    nombre = "Carlos"
    peso_kg = 85
    altura_m = 1.80

    # ** es el operador de potencia en Python (en Java sería Math.pow)
    imc = peso_kg / (altura_m ** 2)

    # :.2f formatea el float con 2 decimales
    print(f"Hola {nombre}.")
    print(f"  Peso:   {peso_kg} kg")
    print(f"  Altura: {altura_m} m")
    print(f"  IMC:    {imc:.2f}")

    # Clasificación según la OMS
    if imc < 18.5:
        categoria = "bajo peso"
    elif imc < 25:
        categoria = "normal"
    elif imc < 30:
        categoria = "sobrepeso"
    else:
        categoria = "obesidad"

    print(f"  Categoría: {categoria}")


if __name__ == "__main__":
    main()

# Función que calcula la media de una lista de números
def calcular_media(numeros: list[float], redondear: bool = False) -> float:
    if not numeros:
        raise ValueError("La lista está vacía, no se puede calcular la media.")
    resultado = sum(numeros) / len(numeros)
    if redondear:
        return round(resultado, 2)
    return resultado


def main():
    numeros = [1.123, 2.456, 3.789, 4.111, 5.555]
    media_sin_redondeo = calcular_media(numeros)
    media_redondeada = calcular_media(numeros, redondear=True)
    print(f"La media de los números sin redondeo es: {media_sin_redondeo}")
    print(f"La media de los números redondeada es: {media_redondeada}")


if __name__ == "__main__":
    main()

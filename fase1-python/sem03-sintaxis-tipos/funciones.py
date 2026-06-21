"""Demostración de funciones en Python: parámetros, defaults, type hints, returns."""


# ====== Función simple, sin parámetros ======
def saludar():
    """Saluda al mundo. No retorna nada (devuelve None implícitamente)."""
    print("¡Hola!")


# ====== Función con parámetros y type hints ======
# Los type hints (int, str, float) NO afectan ejecución, son documentación
# para el editor, el type checker (Pyright), y para ti.
def sumar(a: int, b: int) -> int:
    """Suma dos enteros y devuelve el resultado."""
    return a + b


# ====== Función con valor por defecto ======
# Si no le pasas 'saludo', usa "Hola".
def saludo_personalizado(nombre: str, saludo: str = "Hola") -> str:
    """Devuelve un saludo formateado."""
    return f"{saludo}, {nombre}."


# ====== Función que retorna múltiples valores (tupla) ======
def min_max(numeros: list[int]) -> tuple[int, int]:
    """Devuelve (mínimo, máximo) de una lista de enteros."""
    return min(numeros), max(numeros)


# ====== Función con parámetros por nombre (keyword args) ======
def crear_persona(nombre: str, edad: int, ciudad: str = "Madrid") -> dict:
    """Crea un dict con los datos de una persona."""
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}


def main():
    # Llamada simple
    saludar()

    # Con argumentos posicionales
    resultado = sumar(3, 4)
    print(f"sumar(3, 4) = {resultado}")

    # Con valor por defecto omitido
    print(saludo_personalizado("Carlos"))

    # Con valor por defecto sobrescrito
    print(saludo_personalizado("Carlos", "Buenos días"))

    # Argumentos POR NOMBRE (más legibles)
    print(saludo_personalizado(nombre="Ana", saludo="¡Hey"))

    # Retorno múltiple con desempaquetado
    mn, mx = min_max([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"min = {mn}, max = {mx}")

    # Argumentos mezclados (posicionales + por nombre)
    p = crear_persona("Luis", 35, ciudad="Barcelona")
    print(f"persona = {p}")

    # Si omites el default, usa "Madrid"
    p2 = crear_persona(nombre="Eva", edad=28)
    print(f"persona2 = {p2}")


if __name__ == "__main__":
    main()

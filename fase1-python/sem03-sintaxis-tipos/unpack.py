"""Unpacking avanzado: *args, **kwargs, y expansión en llamadas."""


# Suma cualquier número de argumentos. Recibe ints via *args.
def suma_todos(*args: int) -> int:
    return sum(args)


# Imprime todos los kwargs como "clave = valor". Recibe **kwargs.
def imprimir_config(**kwargs) -> None:
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


# Combina posicionales, *args, y **kwargs en una sola firma.
# Los tres tipos en orden: nombre (obligatorio), *hobbies (variable), **datos_extra (variable con nombre)
def crear_perfil(nombre: str, *hobbies: str, **datos_extra) -> dict:
    perfil = {"nombre": nombre, "hobbies": list(hobbies)}
    perfil.update(datos_extra)
    return perfil


def main():
    # Llamadas con *args
    print("=== *args ===")
    print(f"suma(1, 2, 3):       {suma_todos(1, 2, 3)}")
    print(f"suma(10, 20):        {suma_todos(10, 20)}")
    print(f"suma() sin args:     {suma_todos()}")

    # Llamadas con **kwargs
    print("\n=== **kwargs ===")
    imprimir_config(host="localhost", puerto=8080, debug=True)

    # Llamada con los tres tipos
    print("\n=== Mezcla ===")
    perfil = crear_perfil(
        "Carlos", "leer", "código", "viajar", edad=44, ciudad="Madrid"
    )
    print(f"Perfil: {perfil}")

    # ==== Expansión en llamadas: * y ** al llamar funciones ====
    print("\n=== Expansión al llamar ===")
    numeros = [5, 10, 15]
    print(f"suma(*numeros):      {suma_todos(*numeros)}")  # expande lista como args

    config = {"host": "prod.server", "puerto": 443, "debug": False}
    imprimir_config(**config)  # expande dict como kwargs


if __name__ == "__main__":
    main()

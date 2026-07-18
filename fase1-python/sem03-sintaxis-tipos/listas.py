"""Listas en Python: slicing, métodos, unpacking, comprehensions."""


# Función que filtra solo los pares de una lista
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]


# Devuelve el cuadrado de cada número de la lista
def cuadrado(lista):
    return [num**2 for num in lista]


# Devuelve solo los números mayores que un umbral
def mayores_que(lista, umbral):
    return [num for num in lista if num > umbral]


# Devuelve una lista de tuplas (numero, "par" o "impar")
def etiquetar(lista):
    return [(num, "par" if num % 2 == 0 else "impar") for num in lista]


# Deuvelve un dict {umero: cuadrado} para los pares de la lista
def dict_pares_cuadrados(lista):
    return {num: num**2 for num in lista if num % 2 == 0}


def main():
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Slicing: [inicio:fin:paso]
    print(f"Original: {nums}")
    print(f"Primeros 3: {nums[:3]}")
    print(f"Ultimos 3: {nums[-3:]}")
    print(f"Del 3 al 6: {nums[2:6]}")
    print(f"Salto de 2: {nums[::2]}")
    print(f"Invertida: {nums[::-1]}")
    print(f"Reverso pares: {nums[::-2]}")

    nums = [1, 4, 7, 12, 15, 20, 33, 42]

    # Comprehensions
    print(f"Pares: {filtrar_pares(nums)}")
    print(f"Cuadrado: {cuadrado(nums)}")
    print(f"Mayores que 10: {mayores_que(nums, 10)}")
    print(f"Etiquetar: {etiquetar(nums)}")
    print(f"Dict pares cuadrados: {dict_pares_cuadrados(nums)}")


if __name__ == "__main__":
    main()

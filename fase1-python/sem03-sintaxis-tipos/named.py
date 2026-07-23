"""namedtuple: tuple con nombres de campos, legibilidad sin ceremonia."""

from collections import namedtuple

# Definir el "tipo" — nombre + lista de campos
Persona = namedtuple("Persona", ["nombre", "edad", "ciudad"])


def main():
    # ====== Crear instancias ======
    p1 = Persona("Carlos", 44, "Madrid")  # posicional
    p2 = Persona(nombre="Ana", edad=30, ciudad="Barcelona")  # por nombre
    p3 = Persona("Luis", ciudad="Valencia", edad=35)  # mezcla

    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")

    # ====== Acceso por atributo ======
    print(f"\nNombre de p1: {p1.nombre}")
    print(f"Edad de p2:   {p2.edad}")

    # ====== Sigue siendo tuple: se puede indexar y desempaquetar ======
    print(f"\np1[0]:              {p1[0]}")  # 'Carlos' — como tuple normal
    nombre, edad, ciudad = p1  # tuple unpacking clásico
    print(f"Unpacked: {nombre}, {edad}, {ciudad}")

    # ====== Es INMUTABLE (como cualquier tuple) ======
    try:
        p1.edad = 45  # ¡Error!
    except AttributeError as e:
        print(f"\nInmutable: {e}")

    # ====== Método útil: _replace() crea una NUEVA namedtuple con cambios ======
    p1_actualizada = p1._replace(edad=45)
    print(f"\nOriginal:     {p1}")
    print(f"Actualizada:  {p1_actualizada}")  # nueva instancia, p1 no cambió

    # ====== Método útil: _asdict() convierte a dict (para JSON/Excel) ======
    print(f"\np1 como dict: {p1._asdict()}")


if __name__ == "__main__":
    main()

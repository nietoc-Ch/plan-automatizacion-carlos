"""dataclass: el POJO moderno de Python."""

from dataclasses import asdict, dataclass, field


# ====== Dataclass básica ======
@dataclass
class Persona:
    """Representa a una persona con datos básicos."""

    nombre: str
    edad: int
    ciudad: str = "Madrid"  # valor por defecto
    hobbies: list[str] = field(default_factory=list)  # default mutable requiere factory


# ====== Dataclass INMUTABLE (frozen=True) ======
@dataclass(frozen=True)
class Punto:
    """Coordenada 2D. Inmutable: nadie puede modificarla tras crearla."""

    x: float
    y: float


def main():
    # ====== Crear instancias ======
    p1 = Persona("Carlos", 44)  # ciudad default, hobbies default vacío
    p2 = Persona("Ana", 30, "Barcelona", ["leer", "código"])
    p3 = Persona(nombre="Luis", edad=35, ciudad="Valencia")

    # ====== __repr__ automático (útil para debug) ======
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")

    # ====== Acceso por atributo ======
    print(f"\nNombre de p2:  {p2.nombre}")
    print(f"Hobbies de p2: {p2.hobbies}")

    # ====== Mutable por defecto ======
    print(f"\nAntes:  p1.edad = {p1.edad}")
    p1.edad = 45  # sí se puede
    p1.hobbies.append("viajar")
    print(f"Después: p1 = {p1}")

    # ====== __eq__ automático — compara campo a campo ======
    a = Persona("Ana", 30, "Barcelona", ["leer", "código"])
    b = Persona("Ana", 30, "Barcelona", ["leer", "código"])
    print(f"\na == b: {a == b}")  # True — dataclass compara campo por campo
    print(f"a is b: {a is b}")  # False — son objetos distintos en memoria

    # ====== Convertir a dict (para JSON, DB, etc.) ======
    print(f"\np1 como dict: {asdict(p1)}")

    # ====== Frozen: intento de modificar debería fallar ======
    pt = Punto(3.0, 4.0)
    print(f"\nPunto: {pt}")
    try:
        pt.x = 100
    except Exception as e:
        print(f"Frozen: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

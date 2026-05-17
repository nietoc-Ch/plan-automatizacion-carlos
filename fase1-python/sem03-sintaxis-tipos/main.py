def main():
    # ====== Tipos básicos (Python los infiere del valor) ======
    nombre = "Carlos"            # str (string)
    edad = 44                    # int (entero, precisión arbitraria)
    altura = 1.80                # float (decimal, doble precisión)
    es_dev = True                # bool (¡mayúscula inicial!)
    favorito = None              # None — equivalente a null en Java

    # ====== type() te dice el tipo de cualquier variable ======
    print(f"nombre   = {nombre!r:<20}  → tipo: {type(nombre).__name__}")
    print(f"edad     = {edad!r:<20}  → tipo: {type(edad).__name__}")
    print(f"altura   = {altura!r:<20}  → tipo: {type(altura).__name__}")
    print(f"es_dev   = {es_dev!r:<20}  → tipo: {type(es_dev).__name__}")
    print(f"favorito = {favorito!r:<20}  → tipo: {type(favorito).__name__}")

    # ====== f-strings: forma moderna de formatear (Python 3.6+) ======
    print()  # línea en blanco
    saludo = f"Hola {nombre}, tienes {edad} años y mides {altura}m."
    print(saludo)

    # ====== Tipo dinámico: reasignar a otro tipo es legal ======
    print()
    edad = "cuarenta y cuatro"   # ahora es str
    print(f"Ahora edad = {edad!r} → tipo: {type(edad).__name__}")

    # ====== Operaciones con strings ======
    print()
    nombre_apellido = nombre + " Nieto"    # concatenación clásica
    grito = nombre.upper()                 # método del objeto str
    longitud = len(nombre)                 # len() es función global
    print(f"Concatenado: {nombre_apellido}")
    print(f"En mayúsculas: {grito}")
    print(f"Longitud: {longitud}")


if __name__ == "__main__":
    main()

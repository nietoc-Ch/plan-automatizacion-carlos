"""Demostración de pathlib: paths como objetos."""

from pathlib import Path


def main():
    # ====== Construir paths ======
    # Path.home() devuelve tu carpeta home
    home = Path.home()
    print(f"Home: {home}")

    # Path.cwd() = current working directory
    cwd = Path.cwd()
    print(f"Cwd:  {cwd}")

    # Componer rutas con el operador '/' (no string concat)
    archivo = cwd / "main.py"
    print(f"Archivo: {archivo}")

    # ====== Inspeccionar ======
    print(f"  ¿existe?:    {archivo.exists()}")
    print(f"  ¿es file?:   {archivo.is_file()}")
    print(f"  ¿es dir?:    {archivo.is_dir()}")
    print(f"  nombre:      {archivo.name}")  # 'main.py'
    print(f"  extensión:   {archivo.suffix}")  # '.py'
    print(f"  sin ext:     {archivo.stem}")  # 'main'
    print(f"  padre:       {archivo.parent}")  # carpeta del archivo

    # ====== Leer/escribir texto sin abrir archivo manualmente ======
    nuevo = cwd / "saludo.txt"
    nuevo.write_text("Hola Carlos, esto lo escribió pathlib.\n")
    contenido = nuevo.read_text()
    print(f"\nContenido de {nuevo.name}: {contenido!r}")

    # ====== Iterar archivos en una carpeta ======
    print(f"\nArchivos Python en {cwd.name}:")
    for py_file in cwd.glob("*.py"):
        print(f"  - {py_file.name}")

    # ====== Iterar todo (incluyendo subcarpetas) con glob recursivo ======
    print(f"\nTodo bajo {cwd.name} (recursivo, primeros 5):")
    for path in list(cwd.rglob("*"))[:5]:
        tipo = "📁" if path.is_dir() else "📄"
        # No usa emojis si no quieres — los pongo solo aquí
        print(f"  {tipo} {path.relative_to(cwd)}")

    # Limpiar el archivo de prueba
    nuevo.unlink()
    print(f"\n{nuevo.name} eliminado.")


if __name__ == "__main__":
    main()

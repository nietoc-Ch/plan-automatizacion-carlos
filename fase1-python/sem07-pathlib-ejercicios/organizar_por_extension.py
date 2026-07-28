import sys
from pathlib import Path


def clasificar_por_extension(archivos: list[Path]) -> dict[str, list[Path]]:
    """
    Clasifica una lista de archivos según su extensión.

    Args:
        archivos: Lista de objetos Path correspondientes a archivos.

    Returns:
        Diccionario donde las claves son extensiones (sin punto) y los valores
        son listas de Paths de archivos con esa extensión. Para archivos sin extensión,
        la clave será 'sin_extension'.
    """
    resultado: dict[str, list[Path]] = {}
    for archivo in archivos:
        if archivo.is_file():
            ext = archivo.suffix[1:] if archivo.suffix else "sin_extension"
            resultado.setdefault(ext, []).append(archivo)
    return resultado


def mover_por_extension(carpeta: Path) -> dict[str, int]:
    """
    Mueve los archivos de la carpeta dada a subcarpetas según su extensión.

    Args:
        carpeta: Path del directorio a procesar.

    Returns:
        Un dict con estadísticas: {extension: cantidad_de_archivos_movidos}
    """
    archivos = [f for f in carpeta.iterdir() if f.is_file()]
    clasificados = clasificar_por_extension(archivos)
    stats: dict[str, int] = {}

    for extension, files in clasificados.items():
        destino = carpeta / extension
        destino.mkdir(parents=True, exist_ok=True)

        for fichero in files:
            destino_archivo = destino / fichero.name
            if destino_archivo.exists():
                # Renombrar añadiendo sufijo para evitar sobrescribir
                stem = fichero.stem
                sufijo = 1
                nueva_ruta = destino / f"{stem}_{sufijo}{fichero.suffix}"
                while nueva_ruta.exists():
                    sufijo += 1
                    nueva_ruta = destino / f"{stem}_{sufijo}{fichero.suffix}"
                destino_archivo = nueva_ruta
            fichero.rename(destino_archivo)
        stats[extension] = len(files)
    return stats


def main():
    """
    Punto de entrada principal. Solicita la carpeta al usuario y ejecuta la organización.
    """
    if len(sys.argv) > 1:
        carpeta_path = Path(sys.argv[1])
    else:
        carpeta_str = input("Introduce la ruta de la carpeta a organizar: ").strip()
        carpeta_path = Path(carpeta_str)
    if not carpeta_path.exists() or not carpeta_path.is_dir():
        print(f"El directorio '{carpeta_path}' no existe o no es un directorio.")
        return

    stats = mover_por_extension(carpeta_path)
    print("Reporte   de archivos movidos:")
    for ext, cantidad in stats.items():
        print(f"Extensión '{ext}': {cantidad} archivo(s) movido(s)")


if __name__ == "__main__":
    main()

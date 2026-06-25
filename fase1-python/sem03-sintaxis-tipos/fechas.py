"""Demostración de datetime: timestamps, formato, parsing, aritmética."""

from datetime import datetime, timedelta


def main():
    # ====== Timestamp actual ======
    ahora = datetime.now()
    print(f"Ahora: {ahora}")
    print(f"Tipo:  {type(ahora).__name__}")

    # ====== Formato a string con strftime ======
    # Códigos: %Y año 4d, %m mes, %d día, %H hora 24, %M min, %S seg
    print("\nFormatos:")
    print(f"  ISO básico:   {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Solo fecha:   {ahora.strftime('%Y-%m-%d')}")
    print(f"  Bonito:       {ahora.strftime('%A, %d %B %Y a las %H:%M')}")

    # ====== ISO format (estándar moderno, recomendado) ======
    print(f"\nISO format:   {ahora.isoformat()}")

    # ====== Parsing: string a datetime ======
    fecha_str = "2026-12-25 10:30:00"
    navidad = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
    print(f"\nParseado '{fecha_str}' → {navidad}")

    # Para ISO format, fromisoformat (más simple)
    navidad_iso = datetime.fromisoformat("2026-12-25T10:30:00")
    print(f"Desde ISO:       {navidad_iso}")

    # ====== Aritmética con timedelta ======
    print("\nAritmética:")
    una_semana = timedelta(days=7)
    print(f"  Hoy:                  {ahora.date()}")
    print(f"  En una semana:        {(ahora + una_semana).date()}")
    print(f"  Hace una semana:      {(ahora - una_semana).date()}")
    print(f"  En 3 días y 2 horas:  {ahora + timedelta(days=3, hours=2)}")

    # ====== Diferencia entre dos fechas ======
    cumpleanos_proximo = datetime(ahora.year + 1, 1, 1)  # 1 enero del año que viene
    diferencia = cumpleanos_proximo - ahora
    print("\nFaltan para el año nuevo:")
    print(f"  Total días:  {diferencia.days}")
    print(f"  Total segs:  {diferencia.total_seconds():.0f}")


if __name__ == "__main__":
    main()

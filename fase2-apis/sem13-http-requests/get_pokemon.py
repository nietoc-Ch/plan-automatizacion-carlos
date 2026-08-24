"""Primer request en Python con la librería requests."""

import requests


def main() -> None:
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    respuesta = requests.get(url)

    # Verificar status
    print(f"Status: {respuesta.status_code}")

    # Parsear JSON automáticamente
    datos = respuesta.json()

    # Extraer info útil
    print(f"Nombre:  {datos['name']}")
    print(f"ID:      {datos['id']}")
    print(f"Altura:  {datos['height']} decímetros")
    print(f"Peso:    {datos['weight']} hectogramos")
    print(f"Tipos:   {', '.join(t['type']['name'] for t in datos['types'])}")


if __name__ == "__main__":
    main()

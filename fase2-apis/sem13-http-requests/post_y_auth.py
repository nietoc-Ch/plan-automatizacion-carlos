"""POST con JSON body y GET con Bearer auth."""

import requests


def crear_post() -> None:
    """POST a JSONPlaceholder con JSON body."""
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
        "title": "Aprendiendo requests",
        "body": "Sesión 18 de mi plan",
        "userId": 1,
    }

    respuesta = requests.post(
        url, json=body
    )  # ← json= auto-serializa y añade Content-Type

    print("=== POST a JSONPlaceholder ===")
    print(f"Status: {respuesta.status_code}")
    print(f"Respuesta: {respuesta.json()}")


def ver_headers_con_auth() -> None:
    """GET a HTTPBin con auth y header custom para verificar qué se manda."""
    url = "https://httpbin.org/headers"
    headers = {
        "Authorization": "Bearer sk-fake-token-abc",
        "X-Custom-Header": "hola-desde-python",
    }

    respuesta = requests.get(url, headers=headers)

    print("\n=== GET a HTTPBin (echo de headers) ===")
    print(f"Status: {respuesta.status_code}")
    datos = respuesta.json()
    for clave, valor in datos["headers"].items():
        print(f"  {clave}: {valor}")


def main() -> None:
    crear_post()
    ver_headers_con_auth()


if __name__ == "__main__":
    main()

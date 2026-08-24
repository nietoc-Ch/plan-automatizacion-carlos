"""Manejo de errores HTTP con requests."""

import requests
from requests.exceptions import HTTPError, RequestException


def modo_manual() -> None:
    """Chequeo manual del status code (verboso)."""
    respuesta = requests.get("https://httpbin.org/status/404")

    if respuesta.status_code == 200:
        print("OK")
    elif 400 <= respuesta.status_code < 500:
        print(f"Error del cliente: {respuesta.status_code}")
    elif 500 <= respuesta.status_code < 600:
        print(f"Error del servidor: {respuesta.status_code}")


def modo_idiomatico() -> None:
    """Con raise_for_status: mucho más limpio."""
    try:
        respuesta = requests.get("https://httpbin.org/status/404")
        respuesta.raise_for_status()  # ← lanza HTTPError si status es 4xx o 5xx
        print("OK")
    except HTTPError as e:
        print(f"HTTPError capturado: {e}")


def con_timeout_y_red() -> None:
    """Timeout y errores de red (no confundir con HTTPError)."""
    try:
        # httpbin.org/delay/N responde tras N segundos → con timeout de 1s falla
        respuesta = requests.get("https://httpbin.org/delay/5", timeout=1)
        respuesta.raise_for_status()
        print("OK")
    except requests.Timeout:
        print("Timeout: el servidor tardó más de lo permitido")
    except requests.ConnectionError:
        print("ConnectionError: no se pudo conectar (DNS, red, servidor caído)")
    except HTTPError as e:
        print(f"HTTPError: {e}")
    except RequestException as e:
        print(f"Otro error de request: {e}")


def main() -> None:
    print("=== Modo manual ===")
    modo_manual()

    print("\n=== Modo idiomático (raise_for_status) ===")
    modo_idiomatico()

    print("\n=== Con timeout y errores de red ===")
    con_timeout_y_red()


if __name__ == "__main__":
    main()

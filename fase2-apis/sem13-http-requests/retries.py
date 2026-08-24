"""Retries automáticos con tenacity."""

import json
import logging

import requests
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

# Configura logging para ver los reintentos
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# Decorador: reintenta hasta 4 veces con espera exponencial entre 1 y 10 segundos
# Solo reintenta si es Timeout, ConnectionError o HTTPError 5xx
@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(
        (requests.Timeout, requests.ConnectionError, requests.HTTPError)
    ),
    before_sleep=before_sleep_log(logger, logging.INFO),
    reraise=True,
)
def get_con_retry(url: str, timeout: int = 3) -> dict:
    """Hace GET al url. Reintenta si falla."""
    respuesta = requests.get(url, timeout=timeout)
    respuesta.raise_for_status()
    return respuesta.json()


def caso_1_falla_siempre() -> None:
    """Un endpoint que siempre devuelve 500. Reintenta 4 veces y falla."""
    print("=== CASO 1: /status/500 (siempre falla) ===")
    try:
        get_con_retry("https://httpbin.org/status/500")
    except requests.HTTPError as e:
        print(f"Falló después de todos los reintentos: {e}")


def caso_2_funciona_a_la_primera() -> None:
    """Un endpoint que siempre funciona. Sin reintentos."""
    print("\n=== CASO 2: /json (funciona a la primera) ===")
    datos = get_con_retry("https://httpbin.org/json")
    print(f"OK: recibí un JSON con {len(datos)} clave(s) de nivel superior")
    print(json.dumps(datos, indent=2, ensure_ascii=False))


def main() -> None:
    caso_1_falla_siempre()
    caso_2_funciona_a_la_primera()


if __name__ == "__main__":
    main()

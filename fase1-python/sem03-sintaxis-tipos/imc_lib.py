"""Lógica pura del IMC: cálculo y clasificación.

Sin I/O. Sin prints. Sin inputs. Solo funciones probables con tests.
"""


def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """Calcula el IMC. Lanza ValueError si los datos no son positivos."""
    if peso_kg <= 0 or altura_m <= 0:
        raise ValueError("peso y altura deben ser positivos")
    return peso_kg / (altura_m**2)


def clasificar_imc(imc: float) -> str:
    """Devuelve la categoría OMS para un valor de IMC."""
    if imc < 18.5:
        return "bajo peso"
    if imc < 25:
        return "normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidad"

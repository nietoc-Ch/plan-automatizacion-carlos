"""Lógica pura del IMC: cálculo y clasificación.

Sin I/O. Sin prints. Sin inputs. Solo funciones probables con tests.
"""

from dataclasses import dataclass


@dataclass
class Persona:
    nombre: str
    peso_kg: float
    altura_m: float
    imc: float = 0.0
    categoria: str = ""

    def __post_init__(self):
        if not self.nombre or self.nombre.strip() == "":
            raise ValueError("nombre no puede estar vacío")


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


def calcular_persona(p: Persona) -> Persona:
    """Devuelve nueva Persona con imc y categoria calculados y redondeados."""
    imc_calc = round(calcular_imc(p.peso_kg, p.altura_m), 2)
    categoria = clasificar_imc(imc_calc)
    return Persona(
        nombre=p.nombre,
        peso_kg=p.peso_kg,
        altura_m=p.altura_m,
        imc=imc_calc,
        categoria=categoria,
    )

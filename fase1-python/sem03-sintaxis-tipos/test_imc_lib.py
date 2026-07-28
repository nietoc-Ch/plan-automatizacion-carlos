"""Tests para imc_lib.py."""

import pytest

from imc_lib import Persona, calcular_imc, clasificar_imc

# ============================================================
# Tests de calcular_imc
# ============================================================


def test_calcular_imc_persona_normal():
    """Persona de 70 kg y 1.75 m → IMC = 22.86."""
    imc = calcular_imc(70.0, 1.75)
    assert imc == pytest.approx(22.86, abs=0.01)


def test_calcular_imc_caso_carlos():
    """Carlos: 85 kg, 1.80 m → IMC = 26.23 (sobrepeso)."""
    imc = calcular_imc(85.0, 1.80)
    assert imc == pytest.approx(26.23, abs=0.01)


def test_calcular_imc_peso_cero_lanza_error():
    """Peso 0 no es válido."""
    with pytest.raises(ValueError, match="positivos"):
        calcular_imc(0, 1.80)


def test_calcular_imc_peso_negativo_lanza_error():
    """Peso negativo no es válido."""
    with pytest.raises(ValueError):
        calcular_imc(-5, 1.80)


def test_calcular_imc_altura_cero_lanza_error():
    """Altura 0 no es válida (evita división por cero)."""
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


# ============================================================
# Tests de Persona: validación de nombre
# ============================================================


def test_persona_nombre_vacio_lanza_error():
    """Crear Persona con nombre vacío lanza ValueError."""
    with pytest.raises(ValueError):
        Persona(nombre="", peso_kg=70, altura_m=1.75)


def test_persona_nombre_solo_espacios_lanza_error():
    """Crear Persona con nombre solo con espacios lanza ValueError."""
    with pytest.raises(ValueError):
        Persona(nombre="   ", peso_kg=70, altura_m=1.75)


# ============================================================
# Tests de clasificar_imc
# ============================================================


def test_clasificar_bajo_peso():
    assert clasificar_imc(17.0) == "bajo peso"


def test_clasificar_normal():
    assert clasificar_imc(22.0) == "normal"


def test_clasificar_sobrepeso():
    assert clasificar_imc(27.0) == "sobrepeso"


def test_clasificar_obesidad():
    assert clasificar_imc(35.0) == "obesidad"


# ============================================================
# Tests de límites (boundary tests) — donde anidan los bugs
# ============================================================


def test_limite_18_5_es_normal():
    """Justo 18.5 ya es 'normal', no 'bajo peso'."""
    assert clasificar_imc(18.5) == "normal"


def test_limite_25_es_sobrepeso():
    """Justo 25 ya es 'sobrepeso', no 'normal'."""
    assert clasificar_imc(25.0) == "sobrepeso"


def test_limite_30_es_obesidad():
    """Justo 30 ya es 'obesidad', no 'sobrepeso'."""
    assert clasificar_imc(30.0) == "obesidad"

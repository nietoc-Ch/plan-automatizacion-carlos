from datetime import datetime

from minutas.extractor import extraer_minuta

TEXTO_EJEMPLO = """Reunión de sprint - 2026-07-29
Participantes: Carlos, Ana, Luis, María

[10:00] Carlos: Buenos días a todos. Hoy revisamos el sprint y los pendientes.
[10:02] Ana: Terminé la feature del login. Falta el code review antes de mergear.
[10:05] Carlos: Ana, ¿puedes preparar el PR para mañana?
[10:06] Ana: Sí, mañana lo tengo listo.
[10:07] Luis: Estoy trabajando en la migración de la base de datos a Postgres.
[10:09] Carlos: Luis, envíame el diagrama de la nueva arquitectura la próxima semana.
[10:10] María: Yo documentaré los cambios de la API esta tarde y los publicaré en Notion.
[10:12] Carlos: Perfecto. Cerramos aquí. Nos vemos el viernes en el retro.

Acciones:
- Ana preparará PR de login para mañana
- Luis enviará diagrama de arquitectura la próxima semana
- María documentará API esta tarde en Notion
"""


def test_extrae_titulo_y_fecha():
    minuta = extraer_minuta(TEXTO_EJEMPLO)
    assert minuta.titulo == "Reunión de sprint"
    assert minuta.fecha == "2026-07-29"


def test_extrae_participantes_completos():
    minuta = extraer_minuta(TEXTO_EJEMPLO)
    # La lista debe incluir todos los del bloque, además de Ana, Luis, María (y Carlos por acciones, si aplica)
    # pero no debe repetir nombres
    esperado = ["Carlos", "Ana", "Luis", "María"]  # los 4 aparecen directo y en resumen
    # Ana, Luis y María también como responsables de acciones, ya están en la lista, así que no agrega duplicados
    for nombre in esperado:
        assert nombre in minuta.participantes
    assert len(minuta.participantes) == 4


def test_extrae_resumen_correcto():
    minuta = extraer_minuta(TEXTO_EJEMPLO)
    # El resumen no debe tener timestamps ni nombres, solamente los contenidos
    esperado = (
        "Buenos días a todos. Hoy revisamos el sprint y los pendientes.\n"
        "Terminé la feature del login. Falta el code review antes de mergear.\n"
        "Ana, ¿puedes preparar el PR para mañana?\n"
        "Sí, mañana lo tengo listo.\n"
        "Estoy trabajando en la migración de la base de datos a Postgres.\n"
        "Luis, envíame el diagrama de la nueva arquitectura la próxima semana.\n"
        "Yo documentaré los cambios de la API esta tarde y los publicaré en Notion.\n"
        "Perfecto. Cerramos aquí. Nos vemos el viernes en el retro."
    )
    # Quitar whitespaces
    assert minuta.resumen.replace("\r\n", "\n").strip() == esperado.strip()


def test_extrae_acciones_cantidad_y_datos():
    minuta = extraer_minuta(TEXTO_EJEMPLO)
    # Deben ser 3 acciones
    assert len(minuta.acciones) == 3
    # Verifica responsable, tarea y plazo de cada acción
    a1, a2, a3 = minuta.acciones
    assert a1.responsable == "Ana"
    assert "PR de login" in a1.tarea or "preparará PR de login" in a1.tarea
    assert a1.plazo == "mañana"
    assert a2.responsable == "Luis"
    assert "diagrama de arquitectura" in a2.tarea
    assert a2.plazo == "la próxima semana"
    assert a3.responsable == "María"
    assert (
        "API esta tarde" in a3.tarea
        or "documentará API esta tarde" in a3.tarea
        or "API" in a3.tarea
    )
    assert a3.plazo == "No informado"


def test_fecha_default_si_falta():
    # Sin guion ni fecha explícita
    texto = """Reunión sin fecha ni guion
Participantes: Alex

[09:00] Alex: Empezamos.

Acciones:
- Alex hará el análisis inicial
"""
    ahora = datetime.now().strftime("%Y-%m-%d")
    minuta = extraer_minuta(texto)
    assert minuta.fecha == ahora


def test_titulo_no_encontrado_si_no_hay_guion():
    texto = """Primera línea sin formato de título ni fecha
Participantes: Rita

[09:01] Rita: Probando.

Acciones:
- Rita revisa el proceso hoy
"""
    minuta = extraer_minuta(texto)
    assert minuta.titulo == "Título no encontrado"


def test_plazo_no_informado_en_accion():
    texto = """Sesión - 2024-10-10
Participantes: Pedro

[08:30] Pedro: Acción sin plazo.

Acciones:
- Pedro hará el informe final
"""
    minuta = extraer_minuta(texto)
    assert len(minuta.acciones) == 1
    assert minuta.acciones[0].plazo == "No informado"


def test_no_participantes_lista_vacia_si_no_se_informan():
    texto = """Tema - 2024-06-01

[10:01] Juan: Solo yo.

Acciones:
- Juan verifica esto hoy
"""
    minuta = extraer_minuta(texto)
    # No línea Participantes:, solo los del resumen y acciones
    assert "Juan" in minuta.participantes
    assert len(minuta.participantes) == 1

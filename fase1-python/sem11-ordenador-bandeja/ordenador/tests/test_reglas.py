from ordenador.modelos import Email, Etiqueta
from ordenador.reglas import clasificar_email


def test_clasificacion_urgente() -> None:
    email = Email(
        remitente="jefe@empresa.com",
        asunto="URGENTE: reunión mañana",
        fecha="2026-07-28",
        cuerpo="Nos vemos a las 9",
    )
    assert clasificar_email(email) == Etiqueta.URGENTE


def test_clasificacion_factura() -> None:
    email = Email(
        remitente="proveedor@empresa.com",
        asunto="Factura del mes de junio",
        fecha="2026-07-27",
        cuerpo="Adjunto factura por servicios",
    )
    assert clasificar_email(email) == Etiqueta.FACTURA


def test_clasificacion_spam() -> None:
    email = Email(
        remitente="noreply@marketing.com",
        asunto="Oferta especial 50% descuento",
        fecha="2026-07-26",
        cuerpo="Aprovecha ya",
    )
    assert clasificar_email(email) == Etiqueta.SPAM


def test_clasificacion_personal() -> None:
    email = Email(
        remitente="amigo@gmail.com",
        asunto="Cena el sábado?",
        fecha="2026-07-26",
        cuerpo="Vengan a casa",
    )
    assert clasificar_email(email) == Etiqueta.PERSONAL


def test_clasificacion_trabajo() -> None:
    email = Email(
        remitente="colega@empresa.com",
        asunto="Notas de la reunión de ayer",
        fecha="2026-07-25",
        cuerpo="Adjunto notas de la reunión",
    )
    assert clasificar_email(email) == Etiqueta.TRABAJO


def test_prioridad_urgente_sobre_factura() -> None:
    email = Email(
        remitente="finance@empresa.com",
        asunto="URGENTE: Factura pendiente",
        fecha="2026-07-28",
        cuerpo="Pago inmediato requerido",
    )
    # Aunque es una factura y urgente, por prioridad debe ser URGENTE
    assert clasificar_email(email) == Etiqueta.URGENTE

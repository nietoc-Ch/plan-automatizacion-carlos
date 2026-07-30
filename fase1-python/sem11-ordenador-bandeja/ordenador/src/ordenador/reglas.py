from ordenador.modelos import Email, Etiqueta

PALABRAS_URGENTE = {"urgente", "urgent", "asap", "prioritario", "prioridad"}
PALABRAS_FACTURA = {"factura", "invoice", "pago", "recibo", "receipt"}
PALABRAS_SPAM = {"oferta", "descuento", "promoción", "gratis", "ganaste"}
DOMINIOS_PERSONALES = ("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com")


def clasificar_email(email: Email) -> Etiqueta:
    """
    Clasifica un email según reglas de prioridad, en el siguiente orden:
    1. URGENTE: si alguna palabra de PALABRAS_URGENTE está en el asunto (case-insensitive).
    2. FACTURA: si alguna palabra de PALABRAS_FACTURA está en el asunto o en el cuerpo (case-insensitive).
    3. SPAM: si el remitente empieza con "noreply@" o "no-reply@" Y alguna palabra de PALABRAS_SPAM está en el asunto (case-insensitive).
    4. PERSONAL: si el remitente termina con algún dominio de DOMINIOS_PERSONALES (case-insensitive).
    5. TRABAJO: valor por defecto si ninguna regla anterior aplica.

    Devuelve la Etiqueta correspondiente.
    """
    asunto = email.asunto.lower()
    cuerpo = email.cuerpo.lower()
    remitente = email.remitente.lower()

    # Regla 1: URGENTE
    if any(palabra in asunto for palabra in PALABRAS_URGENTE):
        return Etiqueta.URGENTE

    # Regla 2: FACTURA
    if any(palabra in asunto for palabra in PALABRAS_FACTURA) or any(
        palabra in cuerpo for palabra in PALABRAS_FACTURA
    ):
        return Etiqueta.FACTURA

    # Regla 3: SPAM
    if remitente.startswith(("noreply@", "no-reply@")) and any(
        palabra in asunto for palabra in PALABRAS_SPAM
    ):
        return Etiqueta.SPAM

    # Regla 4: PERSONAL
    if any(remitente.endswith(dominio) for dominio in DOMINIOS_PERSONALES):
        return Etiqueta.PERSONAL

    # Regla 5: TRABAJO (default)
    return Etiqueta.TRABAJO

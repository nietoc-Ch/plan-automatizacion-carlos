import re
from datetime import datetime

from .modelos import Accion, Minuta


def extraer_minuta(texto: str) -> Minuta:
    """
    Extrae una minuta a partir de la transcripción en texto plano según las reglas descritas.

    Args:
        texto (str): Transcripción en texto plano de una reunión.

    Returns:
        Minuta: objeto Minuta poblado con título, fecha, participantes, resumen y acciones.
    """
    # Constantes de expresiones temporales (orden de más largo a más corto)
    expresiones_temporales = [
        "la próxima semana",
        "la semana próxima",
        "la semana que viene",
        "la otra semana",
        "esta tarde",
        "esta mañana",
        "esta noche",
        "el próximo lunes",
        "el próximo martes",
        "el próximo miércoles",
        "el próximo jueves",
        "el próximo viernes",
        "el próximo sábado",
        "el próximo domingo",
        "el lunes",
        "el martes",
        "el miércoles",
        "el jueves",
        "el viernes",
        "el sábado",
        "el domingo",
        "mañana",
        "hoy",
    ]
    # Expresión regular ISO date
    regex_fecha_iso = r"\d{4}-\d{2}-\d{2}"

    lineas = [linea.strip() for linea in texto.strip().split("\n") if linea.strip()]

    # Si texto vacío: valores por defecto
    if not lineas:
        fecha = datetime.now().strftime("%Y-%m-%d")
        return Minuta(
            titulo="Título no encontrado",
            fecha=fecha,
            participantes=[],
            resumen="",
            acciones=[],
        )

    # 1. TÍTULO Y FECHA (primera línea)
    primera = lineas[0]
    match = re.match(r"^(.*?)[\s\-–—]+(" + regex_fecha_iso + r")$", primera)
    if match:
        titulo = match.group(1).strip() or "Título no encontrado"
        fecha = match.group(2)
    else:
        # buscar fecha suelta
        match_fecha = re.search(regex_fecha_iso, primera)
        if match_fecha:
            fecha = match_fecha.group(0)
            antes = primera[: match_fecha.start()]
            titulo = antes.strip() if antes else "Título no encontrado"
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
            titulo = "Título no encontrado"

    # 2. PARTICIPANTES (buscar línea "Participantes: ...")
    participantes: list[str] = []
    idx_participantes = None
    for idx, linea in enumerate(lineas[1:], start=1):
        m = re.match(r"^Participantes\s*:\s*(.+)$", linea, re.IGNORECASE)
        if m:
            participantes = [n.strip() for n in m.group(1).split(",") if n.strip()]
            idx_participantes = idx
            break

    # Identificadores de bloques
    idx_acciones = None
    for i, l in enumerate(lineas):
        if re.match(r"^Acciones\s*:", l, re.IGNORECASE):
            idx_acciones = i
            break

    # 3. RESUMEN (entre participantes y acciones, solo "[hh:mm] Nombre: contenido")
    resumen_lines = []
    nombres_resumen = set()
    resumen_pat = re.compile(
        r"^\[(\d{1,2}:\d{2})\]\s*([\wÁÉÍÓÚÑáéíóúüÜ\-.]+)\s*:\s*(.+)$"
    )
    resumen_inicio = (idx_participantes + 1) if idx_participantes is not None else 1
    resumen_fin = idx_acciones if idx_acciones is not None else len(lineas)

    for linea in lineas[resumen_inicio:resumen_fin]:
        m = resumen_pat.match(linea)
        if m:
            nombre = m.group(2).strip()
            contenido = m.group(3).strip()
            resumen_lines.append(contenido)
            nombres_resumen.add(nombre)
    resumen = "\n".join(resumen_lines).strip()

    # 4. ACCIONES
    acciones: list[Accion] = []
    responsables_acciones = set()
    if idx_acciones is not None:
        acciones_lines = lineas[idx_acciones + 1 :]
        for l in acciones_lines:
            m = re.match(r"^-+\s*(\w+)\s+(.+)$", l)
            if not m:
                continue
            responsable = m.group(1).strip()
            responsables_acciones.add(responsable)
            resto = m.group(2).strip()
            # Buscar expresión temporal en las últimas 3 palabras
            palabras = resto.lower().rsplit(" ", maxsplit=3)
            encontrado = None
            for expr in expresiones_temporales:
                expr_l = expr.lower()
                joined = " ".join(palabras[-len(expr_l.split()) :])
                if len(expr_l.split()) <= len(palabras):
                    texto_final = " ".join(palabras[-len(expr_l.split()) :])
                else:
                    texto_final = " ".join(palabras)
                if texto_final.strip() == expr_l:
                    encontrado = expr
                    break
            tarea = ""
            plazo = ""
            if encontrado:
                expr_idx = resto.lower().rfind(encontrado.lower())
                tarea = resto[:expr_idx].strip()
                plazo = encontrado
            else:
                # Buscar si alguna expresión aparece en las últimas 3 palabras (case-insensitive)
                palabras_resto = resto.split()
                plazo = "No informado"
                tarea = resto
                for expr in expresiones_temporales:
                    expr_pal = expr.lower().split()
                    if len(palabras_resto) >= len(expr_pal):
                        if [
                            w.lower() for w in palabras_resto[-len(expr_pal) :]
                        ] == expr_pal:
                            expr_idx = len(palabras_resto) - len(expr_pal)
                            tarea = " ".join(palabras_resto[:expr_idx]).strip()
                            plazo = expr
                            break
            if not tarea:
                tarea = resto
            acciones.append(Accion(responsable=responsable, tarea=tarea, plazo=plazo))

    # Al final: la lista de participantes incluye sin duplicar los de línea "Participantes:",
    # los nombres encontrados en el resumen, y responsables de acciones
    # Conserva el orden como aparecen originalmente
    participantes_final = []
    agregados = set()
    for nombre in participantes + list(nombres_resumen) + list(responsables_acciones):
        if nombre and nombre not in agregados:
            participantes_final.append(nombre)
            agregados.add(nombre)

    return Minuta(
        titulo=titulo,
        fecha=fecha,
        participantes=participantes_final,
        resumen=resumen,
        acciones=acciones,
    )

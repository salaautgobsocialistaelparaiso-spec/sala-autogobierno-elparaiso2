import urllib.parse

def generar_enlace_whatsapp(numero_telefono: str, mensaje: str) -> str:
    """Genera un enlace directo para enviar el reporte vía WhatsApp Web/App."""
    texto_codificado = urllib.parse.quote(mensaje)
    return f"https://api.whatsapp.com/send?phone={numero_telefono}&text={texto_codificado}"
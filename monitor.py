import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

mensaje = """
✅ FASE 2 ACTIVADA

Monitor configurado para:

✅ Pasaportes
✅ Registro nacimiento
✅ DNI
✅ Autorización de viaje de menor
✅ Carta poder

Playwright instalado correctamente.
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

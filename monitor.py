from datetime import datetime
import requests
import os

# Horario activo: 15:30 a 00:30
ahora = datetime.now()
hora_actual = ahora.hour * 60 + ahora.minute

inicio = 15 * 60 + 30  # 15:30
fin = 30               # 00:30

if not (hora_actual >= inicio or hora_actual <= fin):
    print("Fuera de horario")
    raise SystemExit

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
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("Mensaje enviado")

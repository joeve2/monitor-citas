import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN:", "OK" if BOT_TOKEN else "VACIO")
print("CHAT_ID:", CHAT_ID)

mensaje = "✅ Monitor funcionando desde GitHub"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("STATUS:", r.status_code)
print("RESPUESTA:", r.text)

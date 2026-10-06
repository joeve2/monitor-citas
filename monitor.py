import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

print("LONGITUD TOKEN:", len(BOT_TOKEN))
print("INICIO TOKEN:", BOT_TOKEN[:10])

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

r = requests.get(url)

print("STATUS:", r.status_code)
print("RESPUESTA:", r.text)

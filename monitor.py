import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

r = requests.get(url)

print("STATUS:", r.status_code)
print("RESPUESTA:", r.text)

from datetime import datetime
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Horario activo
ahora = datetime.now()
hora_actual = ahora.hour * 60 + ahora.minute

inicio = 15 * 60 + 30
fin = 30

if not (hora_actual >= inicio or hora_actual <= fin):
    print("Fuera de horario")
    raise SystemExit

BRANCH_ID = "f16e4735888f68606f069193ef218172252eacbe0cbfb4ce15f22fbd4405fe1f"

SERVICIOS = {
    "Pasaportes": "a75954e48a3b6e729b9831d2a3490bc0f933654be616214740ef1a733351c7c0",
    "Registro nacimiento": "78b5e278a273cbab6a3f577fb215fe91610dbe7914c87af0c7bf8858058eb776",
    "DNI": "dd5601892d3df8accd5684c2840ae2c743d757b09dde3e1c68676ace1aba165d",
    "Autorización viaje menor": "951ea200df58f3bd229be821c5b944e867d73d6ad61ea61d9dd94e1bceefc4b84",
    "Carta poder": "d625caa14e41a7bc5e558d9a22081642f626ff022300d7130675a5cbb79aece8"
}

disponibles = []

for nombre, service_id in SERVICIOS.items():

    url = (
        f"https://cita.consuladoperumadrid.org/qmaticwebbooking/"
        f"rest/schedule/branches/{BRANCH_ID}/dates;"
        f"servicePublicId={service_id};customSlotLength=12"
    )

    try:
        r = requests.get(url, timeout=30)

        if r.status_code == 200:

            datos = r.json()

            if datos:
                disponibles.append(nombre)

    except Exception as e:
        print(nombre, e)
 print("Servicios con citas:",disponibles)

if disponibles:

    mensaje = "🚨 CITA DISPONIBLE\n\n"

    for servicio in disponibles:
        mensaje += f"✅ {servicio}\n"

    mensaje += (
        "\nConsulado de Perú en Madrid\n"
        "https://cita.consuladoperumadrid.org/qmaticwebbooking/#/"
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensaje
        }
    )

    print("ALERTA ENVIADA")

else:
    print("Sin citas disponibles")

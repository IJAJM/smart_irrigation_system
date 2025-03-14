import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from sensors.read_sensors import read_sensors

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

def send_telegram_alert(message):
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(TELEGRAM_API_URL, data=payload)

def check_soil_moisture():
    data = read_sensors()
    if data["soil_moisture"] == 0:
        send_telegram_alert("⚠️ Tanah kering! Menyalakan pompa.")
    else:
        send_telegram_alert("✅ Tanah cukup lembab.")

if __name__ == "__main__":
    check_soil_moisture()

import requests
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram alert error: {e}")

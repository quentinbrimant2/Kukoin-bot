import os
import time
from kucoin.client import Client
import requests

# Variables d'environnement
KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = Client(KUCOIN_API_KEY, KUCOIN_API_SECRET, KUCOIN_API_PASSPHRASE)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Erreur Telegram:", e)

def main():
    send_telegram_message("🤖 Bot KuCoin démarré !")

    while True:
        try:
            balance = client.get_account_list(currency='BTC')
            btc_balance = next((item for item in balance if item['currency'] == 'BTC'), None)
            if btc_balance:
                message = f"Solde BTC disponible : {btc_balance['available']}"
                print(message)
                send_telegram_message(message)
            else:
                print("Aucun solde BTC trouvé.")

            time.sleep(60)

        except Exception as e:
            send_telegram_message(f"⚠️ Erreur : {str(e)}")
            time.sleep(30)

if __name__ == "__main__":
    main()

import os
import time
import requests
from kucoin.client import Market, Trade

# Vérification des variables
required_vars = ["KUCOIN_API_KEY", "KUCOIN_API_SECRET", "KUCOIN_API_PASSPHRASE", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
missing_vars = [v for v in required_vars if os.getenv(v) is None]

if missing_vars:
    print(f"❌ Variables manquantes : {', '.join(missing_vars)}")
    exit(1)

# Récupération des variables
KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Initialisation clients KuCoin
market_client = Market()
trade_client = Trade(key=KUCOIN_API_KEY, secret=KUCOIN_API_SECRET, passphrase=KUCOIN_API_PASSPHRASE)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})
    except Exception as e:
        print(f"Erreur Telegram : {e}")

def main():
    print("✅ Bot démarré...")
    send_telegram_message("🤖 Bot KuCoin démarré avec succès !")
    while True:
        try:
            balances = trade_client.get_accounts()
            btc_balance = [b for b in balances if b['currency'] == 'BTC']
            if btc_balance:
                send_telegram_message(f"✅ BTC disponible : {btc_balance[0]['balance']}")
            
            ticker = market_client.get_ticker('BTC-USDT')
            send_telegram_message(f"📈 Prix BTC : {ticker['price']} USDT")
            
            time.sleep(60)
        except Exception as e:
            send_telegram_message(f"⚠️ Erreur : {e}")
            print(f"Erreur : {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()

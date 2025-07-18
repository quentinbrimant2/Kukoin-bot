# Bot KuCoin simple avec notifications Telegram

## Installation

1. Crée un compte KuCoin et génère ta clé API (avec permission trade).
2. Crée un bot Telegram et récupère ton `TELEGRAM_BOT_TOKEN` et ton `TELEGRAM_CHAT_ID`.
3. Configure les variables d’environnement sur Render ou localement :
   - KUCOIN_API_KEY
   - KUCOIN_API_SECRET
   - KUCOIN_API_PASSPHRASE
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHAT_ID

## Déploiement

Pousse ce repo sur GitHub, connecte Render à ce repo et déploie.

---

Le bot envoie une notification au démarrage, puis toutes les 60 secondes le solde BTC disponible sur ton compte KuCoin.

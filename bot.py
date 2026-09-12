import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "@mql5club"

# دریافت قیمت نقره XAG/USD
url = "https://xaus.com/api/v1/spot"

response = requests.get(url, timeout=20)
response.raise_for_status()

data = response.json()

price = float(data["silver_usd_oz"])

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

message = (
    "🥈 قیمت جهانی نقره\n"
    "━━━━━━━━━━━━━━\n\n"
    f"💰 قیمت هر اونس: ${price:,.2f}\n\n"
    f"🕐 زمان: {now}\n\n"
    "#نقره #XAGUSD #Silver"
)

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=20
)

r.raise_for_status()

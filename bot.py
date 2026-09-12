import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "@mql5club"

# دریافت قیمت XAU/USD
url = "https://api.goldprice.dev/v1/prices?symbol=XAU-USD-SPOT"

response = requests.get(url, timeout=20)
response.raise_for_status()

data = response.json()
row = data["symbols"][0]

if row.get("is_stale"):
    raise RuntimeError("Gold price is stale")

price = float(row["price"])

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

message = (
    "🟡 XAU/USD\n\n"
    f"💰 Price: ${price:,.2f}\n"
    f"🕐 {now}\n"
    "#XAUUSD #GOLD"
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

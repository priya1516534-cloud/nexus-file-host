import os

# Admin Configuration
ADMIN_PASSWORD = "MY_SECRET_PASS"  # Isse change kar lena

# Telegram Config (Render Dashboard mein dalna)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
PORT = int(os.environ.get("PORT", 5000))

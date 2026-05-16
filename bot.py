import telebot
from config import BOT_TOKEN, CHANNEL_ID

# Bot initialize ho raha hai
bot = telebot.TeleBot(BOT_TOKEN)

def upload_to_telegram(file_path):
    """File ko Telegram channel par safe tarike se host karne ka system"""
    try:
        with open(file_path, 'rb') as f:
            # send_document har tarah ki file (jaise .py, .zip, .apk) support karta hai
            msg = bot.send_document(CHANNEL_ID, f)
        
        # File ID aur Message ID return karega taaki link ban sake
        return msg.document.file_id, msg.message_id
    except Exception as e:
        print(f"Telegram Engine Error: {e}")
        return None, None

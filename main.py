import telebot
from flask import Flask
import threading
import os

TOKEN = '5055617513:AAFj9oIxKCXKCEk-hRNnoPLx1ufd14KfR9I'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "SHADOW SYSTEM ONLINE", 200

def run_bot():
    bot.remove_webhook()
    bot.infinity_polling()

if __name__ == "__main__":
    # تشغيل البوت في مسار منفصل لكي لا يتوقف السيرفر
    threading.Thread(target=run_bot).start()
    # تشغيل سيرفر الويب
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

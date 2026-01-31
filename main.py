import telebot
from flask import Flask
import threading
import os

# التوكن الجديد (المفتاح السيادي)
TOKEN = '5055617513:AAFj9oIxKCXKCEk-hRNnoPLx1ufd14KfR9I'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "SYSTEM ONLINE 🚀", 200

def start_polling():
    # قتل أي جلسات قديمة متبقية في سيرفرات تليجرام
    bot.remove_webhook()
    print("Starting Giant Engine...")
    bot.infinity_polling()

if __name__ == "__main__":
    # تشغيل البوت في مسار مستقل (Thread) لضمان عدم توقف الويب
    threading.Thread(target=start_polling, daemon=True).start()
    
    # تشغيل منفذ الويب الذي يطلبه رندر
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

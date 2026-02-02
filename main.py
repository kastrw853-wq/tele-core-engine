import telebot
from flask import Flask
import os

# تأكد من الحصول على توكن جديد كلياً (New Token) من BotFather
TOKEN = 'ضع_هنا_التوكن_الجديد_حصراً'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def check():
    return "ENGINE STATUS: ACTIVE", 200

# تشغيل بسيط جداً لضمان النشر
if __name__ == "__main__":
    # تشغيل البوت بدون Threading في البداية للتجربة
    print("Trying to wake up the Giant...")
    port = int(os.environ.get("PORT", 10000))
    # سنكتفي بفتح المنفذ أولاً ليرى رندر أننا "Live"
    app.run(host='0.0.0.0', port=port)

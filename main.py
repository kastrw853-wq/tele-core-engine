import os
import time
import telebot
from flask import Flask
from threading import Thread

# --- إعدادات النواة السيادية ---
TOKEN = '5055617513:AAFj9oIxKCXKCEk-hRNnoPLx1ufd14KfR9I'
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
app = Flask(__name__)

@app.route('/')
def home():
    return "CORE STATUS: ACTIVE 🛰️", 200

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# --- معالجة الأوامر ---
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "✅ **تم تفعيل المحرك الجديد بنجاح.**\nأرسل الرقم الدولي الآن لبدء الفحص.")

@bot.message_handler(func=lambda m: True)
def info_scan(message):
    target = message.text.strip()
    wa_link = f"https://wa.me/{target.replace('+', '')}"
    bot.reply_to(message, f"📡 **تقرير الارتباط لـ {target}:**\n\n🔗 الرابط المباشر: {wa_link}")

if __name__ == "__main__":
    # تشغيل سيرفر الويب في الخلفية لتجنب إغلاق Render للمشروع
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
    
    # تنظيف الـ Webhook القديم وبدء الاتصال الإجباري
    bot.remove_webhook()
    print("🛰️ البوت يعمل الآن بقوة التوكن الجديد...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

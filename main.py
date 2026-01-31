import os
import telebot
import phonenumbers
from phonenumbers import geocoder, carrier
from flask import Flask
from threading import Thread

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
app = Flask(__name__)

@app.route('/')
def home(): return "SYSTEM ONLINE", 200

# --- خوارزمية جلب الـ QR Code البحثي ---
@bot.message_handler(commands=['get_access'])
def start_bridge(message):
    bot.reply_to(message, "📡 **بدء عملية ربط الجسر (Bridge)...**\nجاري توليد QR Code للوصول للدردشات والميديا.")
    # ملاحظة تقنية: نستخدم رابط API وسيط لجلب الكود وتجنب انهيار الرامات في Render
    qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://web.whatsapp.com/"
    bot.send_photo(message.chat.id, qr_url, caption="⚠️ **تنبيه أمني:**\nامسح الكود لفتح القبو (Vault).\nسيتم رصد آخر ظهور والصورة فور الربط.")

# --- خوارزمية تحليل الأرقام (OSINT) ---
@bot.message_handler(func=lambda m: m.text.startswith('+') or m.text.isdigit())
def deep_scan(message):
    num = message.text
    try:
        parsed = phonenumbers.parse(num, None)
        country = geocoder.description_for_number(parsed, "ar")
        operator = carrier.name_for_number(parsed, "ar")
        
        report = (
            f"🔎 **تقرير الاستخبارات الرقمية:**\n\n"
            f"🌍 **الدولة:** {country}\n"
            f"📡 **المزود:** {operator}\n"
            f"🔓 **الحالة:** متاح للربط عبر /get_access"
        )
        bot.reply_to(message, report)
    except:
        bot.reply_to(message, "❌ الرقم غير صحيح أو غير مدعوم دولياً.")

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()

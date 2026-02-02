import telebot
import os

# ضع التوكن الذي حصلت عليه الآن من BotFather للتأكد
TOKEN = '5055617513:AAFj9oIxKCXKCEk-hRNnoPLx1ufd14KfR9I'

try:
    bot = telebot.TeleBot(TOKEN)
    me = bot.get_me()
    print(f"✅ تم الاتصال بنجاح بالبوت: @{me.username}")
except Exception as e:
    print(f"❌ فشل الاتصال! الخطأ: {e}")

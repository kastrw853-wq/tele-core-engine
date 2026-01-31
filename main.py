@bot.message_handler(commands=['get_access'])
def send_qr(message):
    bot.send_message(message.chat.id, "⏳ جاري توليد كود الوصول للقبو (Vault)...")
    from bridge import generate_auth_qr
    qr_img = generate_auth_qr()
    bot.send_photo(message.chat.id, qr_img, caption="⚠️ قم بمسح الكود خلال 30 ثانية للوصول للدردشات.")

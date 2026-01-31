import logging
import time

# إعداد السجلات البرمجية
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("CoreGuard")

def safe_execution(func):
    """معالج يحمي الوظائف من الانهيار المفاجئ"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"⚠️ خلل تقني تم رصده: {str(e)}")
            time.sleep(5) # تهدئة العمليات قبل إعادة المحاولة
            return None
    return wrapper

if __name__ == "__main__":
    print("🛡️ درع الحماية الذاتي جاهز للعمل...")

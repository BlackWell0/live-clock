from flask import Flask
from threading import Thread
import datetime
import pytz
import time
import telegram

مشخصات ربات شما
BOT_TOKEN = "7698118649:AAFd5JREHFqDQT0ormCsLmlqvDiZZOV5iQo"
CHANNEL_ID = "@im_sadegh" # آیدی عددی کانال (حتماً با -100 شروع بشه)

bot = telegram.Bot(token=BOT_TOKEN)

تابع ارسال و ویرایش ساعت
def send_or_update():
msg = bot.send_message(chat_id=CHANNEL_ID, text="⏰ در حال بارگذاری ساعت...")
while True:
tehran = pytz.timezone("Asia/Tehran")
now = datetime.datetime.now(tehran).strftime("%H:%M:%S")
try:
bot.edit_message_text(chat_id=CHANNEL_ID,
message_id=msg.message_id,
text=f"⏰ ساعت اکنون (ایران): {now}")
except Exception as e:
print("خطا در ویرایش پیام:", e)
time.sleep(1)

برای آنلاین نگه‌داشتن Replit
app = Flask('')

@app.route('/')
def home():
return "ربات فعال است."

def run():
app.run(host='0.0.0.0', port=5000)

اجرای همه چیز با Thread
if name == 'main':
Thread(target=run).start()
Thread(target=send_or_update).start()
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------
# Config
# -----------------------------
CFLR_URL = "https://tse-bot.mehdihassani3051.workers.dev/?text="

# -----------------------------
# Dummy data / placeholders
# Replace these with actual tsetmc fetching logic
# -----------------------------
ih = []  # لیست داده‌های سهام
ct = {}  # اطلاعات خریدار/فروشنده
pl = 0   # قیمت پایانی
pc = 0   # قیمت آخرین معامله
tvol = 0 # حجم کل
tval = 0 # ارزش کل
is5 = 1  # میانگین حجم برای فیلتر
stochk = 0
st60 = 0
RSI_CUR = 0
ghodrat = 0
skharid = 0
sforosh = 0
darsadk = 0
darsadf = 0
mony = ""
l18 = "نماد"  # نام سهم
pe = 0
plp = 0
pcp = 0
S1 = 0
post_n = ""

# -----------------------------
# Helper functions
# -----------------------------
def TseHitSender(txtmessage):
    try:
        url = CFLR_URL + requests.utils.quote(txtmessage)
        requests.get(url)
    except Exception as e:
        print("Error sending message:", e)

def addCommas(a, c=2):
    a = str(a)
    x = a.split(".")
    x1 = x[0]
    x2 = "." + x[1][:c] if len(x) > 1 and int(x[1]) != 0 else ""
    while True:
        import re
        b = re.search(r"(\d+)(\d{3})", x1)
        if not b: break
        x1 = re.sub(r"(\d+)(\d{3})", r"\1,\2", x1)
    return x1 + x2

# -----------------------------
# Filters (placeholder logic)
# Implement your exact calculations here
# -----------------------------
x1 = True  # مثال: فقط برای تست ارسال پیام

# -----------------------------
# Compose message
# -----------------------------
ntime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
post_n = f"✅نماد: {l18}\n⏰ {ntime}\nفیلتر ۱ فعال است!"

# -----------------------------
# Send message if any filter active
# -----------------------------
if x1:  # اگر فیلتر فعال است
    TseHitSender(post_n)

print("Message sent:", post_n)


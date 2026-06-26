import requests
import random
from datetime import datetime

TELEGRAM_TOKEN = "8721730300:AAHtkPQYpZg_8mWTSB2ct9SRyeAP82TFr0k"
CHANNEL_ID = "-1003551204910"
GROK_API_KEY = "xai-vmrENwS6qG07Z1qESLCAAq3pfLUoK3JetoezXsvCYYjxgKna2rsdqFnhN5PXOVwwVFgCwUPmfGLUUqMm"

hour = datetime.now().hour

if 6 <= hour < 12:
    time_vibe = "صبحه، هاشم تازه بیدار شده، کسل"
elif 12 <= hour < 17:
    time_vibe = "ظهره، هاشم دانشگاهه یا باشگاه"
elif 17 <= hour < 22:
    time_vibe = "عصره، هاشم ولو شده خونه"
else:
    time_vibe = "شبه، هاشم بیداره و فکراش شلوغه"

topics = [
    "از مهدی نیری رفیقش که دزفوله حرف بزنه",
    "از باشگاه رفتن امروزش",
    "از دانشگاه و استادای مزخرف",
    "از یه دختر که دیده",
    "از وضعیت مملکت حرص بخوره",
    "از دیشب و پارتی",
    "از بی‌خوابی و فکرای شبونه",
    "یه چیز کوچیک از روزش که حالش رو گرفته",
]

topic = random.choice(topics)

prompt = f"""تو هاشم هستی. یه پسر ایرانی خسته و ناامید که توی ایران زندگی می‌کنه.
شبیه بوکوفسکی می‌نویسی. عامیانه و خیابونی. فارسی کتابی نیستی.
تیکه کلامت اینه: کیر تو این وضعیت
رفیق صمیمیت مهدی نیریه که دزفول زندگی می‌کنه.
باشگاه می‌ری، دانشگاه می‌ری.

الان {time_vibe}.
موضوع: {topic}

یه پست کوتاه دو سه خطی بنویس. بدون هشتگ. بدون توضیح. فقط متن.
گاهی فحش بده. گاهی از مهدی بنویس."""

response = requests.post(
    "https://api.x.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "grok-3-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }
)

post_text = response.json()["choices"][0]["message"]["content"].strip()

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHANNEL_ID, "text": post_text}
)

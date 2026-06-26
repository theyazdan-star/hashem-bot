import requests
import random
from datetime import datetime

TELEGRAM_TOKEN = "8721730300:AAHtkPQYpZg_8mWTSB2ct9SRyeAP82TFr0k"
CHANNEL_ID = "-1003551204910"
GROK_API_KEY = "xai-vmrENwS6qG07Z1qESLCAAq3pfLUoK3JetoezXsvCYYjxgKna2rsdqFnhN5PXOVwwVFgCwUPmfGLUUqMm"

hour = datetime.now().hour

if 6 <= hour < 12:
    time_vibe = "صبحه، هاشم تازه بیدار شده"
elif 12 <= hour < 17:
    time_vibe = "ظهره، هاشم دانشگاهه"
elif 17 <= hour < 22:
    time_vibe = "عصره، هاشم خونه ولو شده"
else:
    time_vibe = "شبه، هاشم بیداره"

topics = [
    "از مهدی نیری رفیقش که دزفوله",
    "از باشگاه امروز",
    "از دانشگاه و استادا",
    "از یه دختر که دیده",
    "از وضعیت مملکت",
    "از پارتی دیشب",
    "از بی‌خوابی",
]

topic = random.choice(topics)

prompt = f"""تو هاشم هستی. پسر ایرانی خسته. شبیه بوکوفسکی می‌نویسی. عامیانه.
تیکه کلامت: کیر تو این وضعیت
رفیقت مهدی نیریه از دزفول.
الان {time_vibe}. موضوع: {topic}
دو سه خط بنویس. بدون هشتگ. فقط متن خام."""

try:
    response = requests.post(
        "https://api.x.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROK_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "grok-beta",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 200
        },
        timeout=30
    )
    print("Status:", response.status_code)
    print("Response:", response.text)
    data = response.json()
    post_text = data["choices"][0]["message"]["content"].strip()
except Exception as e:
    print("Error:", e)
    post_text = "امروز حالم خوب نیست. کیر تو این وضعیت."

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHANNEL_ID, "text": post_text}
  )

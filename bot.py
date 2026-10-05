import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 أهلاً بك في بوت حماية واتساب!\n\n"
        "سأساعدك على تعلم طرق حماية حسابك وخصوصيتك."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app_web = Flask(__name__)
@app_web.route("/")
def home():
    return "Bot is running"

Thread(target=lambda: app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()
app.run_polling()

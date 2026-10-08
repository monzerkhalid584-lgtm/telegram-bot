import os
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🛡️ كيف تبند قنوات تيليجرام",
            callback_data="report"
        )],
        [InlineKeyboardButton(
            "🔢 كيفية معرفة رقمك التسلسلي وما الفائدة منه",
            callback_data="serial"
        )]
    ]

    await update.message.reply_text(
        "🔐 أهلاً بك في البوت!\n\nاختر من القائمة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "report":
        text = """
🔒 طريقة الإبلاغ عن المحتوى المخالف في تيليجرام

يمكنك فتح المحتوى المخالف واستخدام خيار الإبلاغ الرسمي داخل تيليجرام، ثم اختيار سبب الإبلاغ المناسب وإرسال البلاغ.

استخدم الإبلاغ فقط عندما يكون المحتوى مخالفًا لقواعد تيليجرام.
"""
        await query.message.reply_text(text)

    elif query.data == "serial":
        await query.message.reply_text(
            "🔢 الرقم التسلسلي هو رقم/معرّف يُستخدم للتعرّف على جهاز أو نظام معين، "
            "وقد يساعد في الدعم الفني أو تتبع معلومات الجهاز حسب الخدمة المستخدمة.\n\n"
            "⚠️ لا تشارك أي رقم تسلسلي أو معرّف جهاز مع أشخاص غير موثوقين."
        )

        try:
            with open("XRecorder_20260819_01.mp4", "rb") as video:
                await query.message.reply_video(video=video)
        except FileNotFoundError:
            await query.message.reply_text(
                "⚠️ الفيديو غير موجود على الخادم."
            )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running"


Thread(
    target=lambda: app_web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
).start()

app.run_polling()

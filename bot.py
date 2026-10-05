import os
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛡️ كيف تبند قنوات تيليجرام", callback_data="report")]
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


شرح الليله طريقه حظر قنوات تيليجرام

------------------------------------------------------------------
• الـطـريـقـه سـاهـلـه و بـسـيـطـه بـس انـت ركـز
بـتـخـش الـقـنـاه بـتـطـلـع لـيـك اول رسـالـه 
بـتـلـقـا بـروفـايـل الـقـنـاه بـتـشـد فـيـهـو بـلاغـات
مـن كـم حـسـاب

• تـانـي بـتـبـلـغ فـي الـرسـالـه الـبـعـد الـبـروفـايـل
و اخـر رسـالـه فـي الـقـنـاه

> شـد بـلاغـات يـسـتـحـسـن 5 حـسـابـات و فـوق
------------------------------------------------------------------

-----------------------------------------------------------------

        """
        await query.message.reply_text(text)

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

import os
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 أهلاً بك في بوت حماية واتساب!\n\n"
        "سأساعدك على تعلم طرق حماية حسابك وخصوصيتك."
    )

app = Application.builder().token(TOKEN).build()
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "report":
        await query.message.reply_text("""الـســلام عــلـيكـم و رحــمه الله

شرح الليله طريقه الإبلاغ عن قنوات تيليجرام 🔒⛔

------------------------------------------------------------------

• الـســلام عــلـيكـم و رحــمه الله

شرح الليله طريقه حظر قنوات تيليجرام🔒⛔

------------------------------------------------------------------
• الـطـريـقـه سـاهـلـه و بـسـيـطـه بـس انـت ركـز
بـتـخـش الـقـنـاه بـتـطـلـع لـيـك اول رسـالـه 
بـتـلـقـا بـروفـايـل الـقـنـاه بـتـشـد فـيـهـو بـلاغـات
مـن كـم حـسـاب

• تـانـي بـتـبـلـغ فـي الـرسـالـه الـبـعـد الـبـروفـايـل
و اخـر رسـالـه فـي الـقـنـاه

> شـد بـلاغـات يـسـتـحـسـن 5 حـسـابـات و فـوق
------------------------------------------------------------------.

• اخـتـار سـبـب الإبـلاغ الـمـنـاسـب،
وأرسـل الـبـلاغ إذا كـان الـمـحـتـوى يـخـالـف قـواعـد تـيـلـيـجـرام.

------------------------------------------------------------------""")

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app_web = Flask(__name__)
@app_web.route("/")
def home():
    return "Bot is running"

Thread(target=lambda: app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()
app.run_polling()

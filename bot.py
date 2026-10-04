from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8936265941:AAEj2l-RZ5Px5Ne0hK6fAbhgwJiGxb228-o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 أهلاً بك في بوت حماية واتساب!\n\n"
        "سأساعدك على تعلم طرق حماية حسابك وخصوصيتك."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

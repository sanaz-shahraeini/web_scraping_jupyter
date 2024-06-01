from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import Anime_scrap

token_ = """7093526457:AAG0YLzuocohWi0Zww7gRB6pI8xl98qgdMA"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Enter name Anime :)",
                                   reply_to_message_id=update.effective_message.id)
async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.effective_message.text.lower()
    card = web_s.search(txt)
    dic = web_s.cards(card)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=dic,
                                   reply_to_message_id=update.effective_message.id)

def anime_bot() -> None:
    application = Application.builder().token(token_).build()
    print("running")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("text", text))
    application.run_polling()


anime_bot()
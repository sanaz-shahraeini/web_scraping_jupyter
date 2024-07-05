import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from decouple import config
import Anime_scrap_web as aw
import anime_gsheet as ag
from random import choice
import pishnehadi as btn

TOKEN = config('token')

# login website
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
aw.login(user="zamir", u_pass="z@mir2000")


# command handler
async def start(update: Update, context: CallbackContext):
    keyboard_start = [
        [InlineKeyboardButton(text="جست و جو🔎", callback_data="name anime"), ],
        [InlineKeyboardButton(text="انیمه پیشنهادی🤌🏻", callback_data="code anime"), ],
        [InlineKeyboardButton(text=f"تصویر زمینه🌃", callback_data="wallpaper")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_start)
    await update.message.reply_text(f"سلام {update.message.from_user.first_name} خوش آمدی",
                                    reply_markup=reply_markup)
    print(update.message.from_user)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "name anime":
        await query.edit_message_text(text=f"نام انیمه خود را به انگلیسی بنویسید.")
    elif query.data == "code anime":
        await context.bot.send_photo(chat_id=query.from_user.id,
                                     photo=btn.img1,
                                     caption=btn.cap1,
                                     reply_markup=btn.replay_markup)
    elif query.data == "wallpaper":
        fil = open("image_url.txt", "r")
        lin = fil.readlines()
        lin = choice(lin)
        await context.bot.send_photo(chat_id=query.from_user.id, photo=lin)
        fil.close()
    else:
        query = update.callback_query
        code_button = query.data
        await query.answer()
        await query.edit_message_text(text="منتظر بمانید ...")
        await code_anime(update, code_button, context)


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text("send your anime name : /name (name anime)")
    # await update.message.reply_text("send your anime code : /code (number)")

dic_result = "for dict"


async def send_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global dic_result
    text: str = update.message.text
    dic_result = aw.cards(aw.search_(text))
    dict_text = open("text_result", "w")
    # Write found links page in a file
    for link in dic_result["href"]:
        dict_text.write(link + "\n")
    dict_text.close()
    number_result = len(dic_result["name"])
    if number_result == 0:
        await update.message.reply_text(f"انیمه ای با این نام پیدا نشد.")
    else:
        fil = open("text_code", "w")
        for i in range(number_result):
            result = dic_result["name"][i]
            fil.write(f"code{i + 1}: {result} \n")
        fil = open("text_code", "r")
        text_codes = fil.read()
        keyboard_code = []
        for i in range(number_result):
            call_back = i
            punch = [InlineKeyboardButton(text=f"{i + 1}", callback_data=call_back)]
            keyboard_code.append(punch)
        print(keyboard_code)
        reply_code = InlineKeyboardMarkup(keyboard_code)
        await update.message.reply_text(f"{text_codes}کد انیمه مورد نظر انتخاب کنید.",
                                        reply_markup=reply_code)
        fil.close()


async def code_anime(update, code_, context):
    query = update.callback_query
    await query.answer()
    number_anime = int(code_)
    number_anime += 1
    result = []
    # Creating a list of link pages
    with open("text_result") as text_result:
        line = text_result.readline()
        i = 1
        while line:
            result.append(line.strip())
            line = text_result.readline()
            i += 1
    number_anime -= 1
    url_anime = result[number_anime]
    list_link = aw.download(url_anime)
    anime_data = []
    for j in list_link:
        anime_data.append(j)
    ag.glinks(anime_data)
    url_img = dic_result["image"][number_anime]
    print(url_img)
    await query.edit_message_text(f"لینک انیمه:  \n {anime_data[1]}\n")

    await query.message.chat.send_message(f"زیر نویس:  \n {anime_data[2]}")


# run bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler((CallbackQueryHandler(button)))
    application.add_handler(MessageHandler(filters.TEXT, send_anime))
    application.add_handler(CallbackQueryHandler(code_anime))
    application.run_polling()

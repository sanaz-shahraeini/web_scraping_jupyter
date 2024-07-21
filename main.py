import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from decouple import config
import Anime_scrap_web as aw
from random import choice
import button as btn
from time import sleep

TOKEN = config('token')
User = config('User')
password = config('Password')
# login website
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
aw.login(user=User, u_pass=password)  # login in website
Counter = 0
Counter2 = 0     # value in news_command and button
dic_result = "for dict"  # dictionary in send_anime and
news_dict = aw.news()

# command handler
async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"""سلام {update.message.from_user.first_name} خوش آمدی.
برای راهنمایی استفاده از ربات می توانی از help/ کمک بگیری             
             """, reply_markup=btn.keyboard_start())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text=btn.help_text,
                                    reply_markup=btn.keyboard_start())


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global news_dict, Counter2
    keyboard = [[InlineKeyboardButton(text="لینک خبر🗞", callback_data="link",
                                      url=news_dict["link"][Counter2])],
                [InlineKeyboardButton(text=f"➡️", callback_data="call_integer")]]
    reply_news = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.message.from_user.id,
                                   text=news_dict["caption"][Counter2],
                                   reply_markup=reply_news)
    news_dict = aw.news()


# command handler

async def send_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global dic_result
    text: str = update.message.text.replace("/name", "")
    dic_result = aw.cards(aw.search_(text))
    dict_text = open("text_result", "w")
    # Write found links page in a file
    for link in dic_result["href"]:
        dict_text.write(link + "\n")
    dict_text.close()
    number_result = len(dic_result["name"])
    if number_result == 0:
        await update.message.reply_text(f"انیمه ای با این نام یافت نشد",
                                        reply_markup=btn.keyboard_start())
    else:
        fil = open("text_code", "w")
        for i in range(number_result):
            result = dic_result["name"][i]
            fil.write(f"{i + 1}: {result} \n")
        fil = open("text_code", "r")
        text_codes = fil.read()
        await update.message.reply_text(text=f"{text_codes}انیمه مورد نظر انتخاب کنید.",
                                        reply_markup=btn.code(number_result))
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
    for link in list_link:
        anime_data.append(link)
    url_img = dic_result["image"][number_anime]
    await context.bot.send_photo(chat_id=query.from_user.id,
                                 photo=url_img,
                                 reply_markup=btn.keyboard_suggested(url_sub=anime_data[1],
                                                                     url_dow=anime_data[0]))


"""
Bot button functionality and responding to them
Most of the buttons are written in the file button.py
Some buttons are inside this file
"""


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "name anime":
        await query.edit_message_text(text=f"نام انیمه خود را به انگلیسی بنویسید.")

    elif query.data == "suggested anime":
        global Counter
        Counter +=1
        if Counter == 3:
            Counter = 0
        await context.bot.send_photo(chat_id=query.from_user.id,
                                     photo=btn.suggested_dict["img"][Counter],
                                     caption=btn.suggested_dict["cap"][Counter],
                                     reply_markup=btn.keyboard_suggested(url_sub=btn.suggested_dict["url_zer"][Counter],
                                                                         url_dow=btn.suggested_dict["url_don"][Counter]))

    elif query.data == "wallpaper":
        fil = open("image_url.txt", "r")
        lin = fil.readlines()
        lin = choice(lin)
        await context.bot.send_photo(chat_id=query.from_user.id, photo=lin)
        fil.close()

    elif query.data == "new":
        await query.edit_message_text(text="منتظر بمانید...")
        list_anime = aw.new_anime()
        for i in range(len(list_anime['title']) // 5):
            link = aw.search_(list_anime['title'][i])
            sleep(2)
            card = aw.cards(link)
            sleep(2)
            try:
                dow = aw.download(card['href'][0])
            except IndexError:
                continue
            await context.bot.send_photo(chat_id=query.from_user.id,
                                         photo=card['image'][0],
                                         caption=card['name'][0],
                                         reply_markup=btn.keyboard_new(url_sub=dow[3], url_dow=dow[1]))
        await query.edit_message_text(text="پایان...")

    elif query.data == "call_integer":
        global news_dict, Counter2
        Counter2 += 1
        if Counter2 < len(news_dict["link"]) - 1:
            keyboard = [[InlineKeyboardButton(text="لینک خبر🗞", callback_data="link",
                                              url=news_dict["link"][Counter2])],
                        [InlineKeyboardButton(text=f"➡️", callback_data="call_integer")]]
            reply_news = InlineKeyboardMarkup(keyboard)
        else:
            keyboard = [[InlineKeyboardButton(text="لینک خبر🗞", callback_data="link",
                                              url=news_dict["link"][Counter2])]]
            reply_news = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(chat_id=query.from_user.id,
                                       text=news_dict["caption"][Counter2],
                                       reply_markup=reply_news)

    else:
        query = update.callback_query
        code_button = query.data
        await query.answer()
        await code_anime(update, code_button, context)


# run bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(MessageHandler(filters.TEXT, send_anime))
    application.add_handler((CallbackQueryHandler(button)))
    application.add_handler(CallbackQueryHandler(code_anime))
    application.run_polling()

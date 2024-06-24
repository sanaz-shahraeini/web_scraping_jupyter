import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from decouple import config
import Anime_scrap_web as sw
import anime_gsheet as ag

TOKEN = config('token')

# login website
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
sw.login(user="zamir", user_pass="z@mir2000")


# command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"welcome {update.message.from_user.first_name}")
    await update.message.reply_text(f"send your anime name type: /name (name anime)\n"
                                    f"send your anime code type: /code (number)\n"
                                    f"if you need help type: /help")
    print(update.message.from_user)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("send your anime name : /name (name anime)")
    await update.message.reply_text("send your anime code : /code (number)")


async def send_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text.replace("/name", "")
    if text == " " or text == "":
        await update.message.reply_text("send your anime name : /name (name anime)")
    else:
        dic_result = sw.cards(sw.search_(text))
        dict_text = open("dict_result", "w")

        # Write found links page in a file
        for link in dic_result["href"]:
            dict_text.write(link + "\n")
        dict_text.close()
        number_result = len(dic_result["name"])
        if number_result == 0:
            await update.message.reply_text(f"The desired anime was not found."
                                            f"Please be careful in writing the name")
        else:
            fil = open("text_code", "w")
            for i in range(number_result):
                result = dic_result["name"][i]
                fil.write(f"code{i + 1}: {result} \n")
            fil = open("text_code", "r")
            text_codes = fil.read()
            await update.message.reply_text(text_codes)
            fil.close()
            await update.message.reply_text(f"Enter code anime , just Number !!")
    print(text)


async def code_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global url_anime
    code: int = update.message.text.replace("/code ", "")
    try:
        code = int(code)
    except ValueError:
        await update.message.reply_text("First enter name anime then Enter a number")
    result = []
    # Creating a list of link pages
    with open("dict_result") as dic_result:
        line = dic_result.readline()
        i = 1
        while line:
            result.append(line.strip())
            line = dic_result.readline()
            i += 1

    if code == 0:
        await update.message.reply_text("send your anime code type: /code (number)")
    else:
        code -= 1
        url_anime = result[code]
    list_link = sw.download(url_anime)
    anime_data = []
    for j in list_link:
        anime_data.append(j)
    ag.glinks(anime_data)
    await update.message.reply_text(f"link download \n {anime_data[1]}")
    await update.message.reply_text(f"subtitle \n {anime_data[2]}")
    print(code)


# run bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('name', send_anime))
    application.add_handler(CommandHandler('code', code_anime))
    application.run_polling()

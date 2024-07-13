from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


img1 = ("https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,"
        "quality=85,width=1200,height=675/catalog/crunchyroll/"
        "ac0052958fa876ed2ef926920a88ec75.jpe")
cap1 = """
    نام انیمه: Fullmetal Alchemist: Brotherhood
    ژانر: ماجراجویی
    تاریخ انتشار: 2009
    خلاصه: دو برادر مادرشان را به دلیل یک بیماری لاعلاج از دست می دهند. آنها با نیروی علم کیمیا،از دانشی ممنوع برای برانگیختن مادرشان استفاده می کنند. اما کار آنها با شکست رو به رو می شودو به عنوان مجازاتی برای استفاده از این گونه کیمیا، برادر بزرگتر، ادوارد الریک پای چپش و برادر کوچکتر، الفونس الریک تمام بدنش را از دست می دهد. ادوارد برای نجات برادرش دست راستش را قربانی می کند و می تواند روح برادرش را به یک زره کامل پیوند بزند و ادوارد با کمک یک دوست خانوادگی اعضای بدن فلزی، “اتومیل”، را دریافت می کند تا آنها را جایگزین اعضای از دست رفته اش کند. با این کار او سوگند یاد می کند که به دنبال اکسیر بگردد تا خود و برادرش را به بدن های اولشان بازگرداند، حتی اگر این بدین معنا باشد که او یک “کیمیاگر ایالت” شود، یعنی کسی که از کیمیا برای ارتش استفاده می کند.
    """

url_zer = "https://dl.animesp.xyz/subs/%5BAnimWorld%5D%20FullMetal%20Alchemist%20BrotherHood.rar"
url_don ="https://dl.animesp.xyz/Completed/Fullmetal%20Alchemist%3A%20Brotherhood/720/"

# _______ button anime suggested ______
def keyboard_suggested(url_sub, url_dow):
    keyboard = [
        [InlineKeyboardButton(text="زیر نویس",
                              url=url_sub),
         InlineKeyboardButton(text="لینک دانلود",
                              url=url_dow)]]

    suggested = InlineKeyboardMarkup(keyboard)
    return suggested


# _______ keyboard button______
def keyboard_button():
    keyboard = [[KeyboardButton("/start"), KeyboardButton("/help")]]
    key = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
    return key


# _____keyboard start ________
def keyboard_start():
    keyboard = [[InlineKeyboardButton(text="جست و جو🔎", callback_data="name anime"),
                InlineKeyboardButton(text="انیمه پیشنهادی🤌🏻", callback_data="code anime")],
                [InlineKeyboardButton(text="جدیدترین انیمه ها🌟", callback_data="new"),
                InlineKeyboardButton(text=f"تصویر زمینه🌃", callback_data="wallpaper")]]
    reply_start = InlineKeyboardMarkup(keyboard)
    return reply_start


#   ______keyboard code ________
def keyboard_code(number_result):
    list_code = []
    for i in range(number_result):
        call_back = i
        punch = [InlineKeyboardButton(text=f"{i + 1}", callback_data=call_back)]
        list_code.append(punch)
    reply_code = InlineKeyboardMarkup(list_code)
    return reply_code


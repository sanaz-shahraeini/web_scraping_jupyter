from telegram import (Update, InlineKeyboardButton,
                      InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)

# _______  CAPTION anime suggested ______
img1 = ("https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,"
        "quality=85,width=1200,height=675/catalog/crunchyroll/"
        "ac0052958fa876ed2ef926920a88ec75.jpe")
cap1 = """
نام انیمه: Fullmetal Alchemist: Brotherhood
ژانر: ماجراجویی
تاریخ انتشار: 2009
خلاصه: دو برادر مادرشان را به دلیل یک بیماری لاعلاج از دست می دهند. آنها با نیروی علم کیمیا،از دانشی ممنوع برای برانگیختن مادرشان استفاده می کنند. اما کار آنها با شکست رو به رو می شودو به عنوان مجازاتی برای استفاده از این گونه کیمیا، برادر بزرگتر، ادوارد الریک پای چپش و برادر کوچکتر، الفونس الریک تمام بدنش را از دست می دهد. ادوارد برای نجات برادرش دست راستش را قربانی می کند و می تواند روح برادرش را به یک زره کامل پیوند بزند و ادوارد با کمک یک دوست خانوادگی اعضای بدن فلزی، “اتومیل”، را دریافت می کند تا آنها را جایگزین اعضای از دست رفته اش کند. با این کار او سوگند یاد می کند که به دنبال اکسیر بگردد تا خود و برادرش را به بدن های اولشان بازگرداند، حتی اگر این بدین معنا باشد که او یک “کیمیاگر ایالت” شود، یعنی کسی که از کیمیا برای ارتش استفاده می کند.
"""
url_zer1 = "https://dl.animesp.xyz/subs/%5BAnimWorld%5D%20FullMetal%20Alchemist%20BrotherHood.rar"
url_don1 ="https://dl.animesp.xyz/Completed/Fullmetal%20Alchemist%3A%20Brotherhood/720/"

img2 = "https://www.film2movie.asia/content/uploads/My_Hero-Academia-S03.jpg"
cap2 ="""
نام انیمه: Boku no Hero Academia
ژانر:اکشن , ماجرایی
تاریخ انتشار: 2016
مدرسه قهرمانانه من ، نام سریالی انیمیشنی می‌باشد که توسط کنجی ناگاساکی ساخته شده است. در خلاصه داستان این سریال آمده است ، ایزوکو یک پسر عادی هست که تنها آرزویش تبدیل شدن به یک قهرمان است. او در دنیایی متولد شده است که هشتاد درصد مردم قدرت ماورائی دارند ، اما ایزوکو جز آن افرادی هست که هیچ قدرتی ندارند. او برای همین همیشه از طرف بچه‌های دیگه مورد تمسخر قرار می‌گیرد. تا اینکه…
"""
url_zer2 = "https://dl.animesp.xyz/subs/%5BAnimWorld%5D%20Boku%20no%20Hero%20Academia%20S01.rar"
url_don2 ="https://dl.animesp.xyz/Completed/Boku%20no%20Hero%20Academia%20S1/720%20x265%20BD/"

img3 = "https://static.wikia.nocookie.net/onepiece/images/8/87/One_Piece_Anime_Logo.png/revision/latest?cb=20140921221019"
cap3 ="""
نام انیمه: One Piece
ژانر:اکشن , ماجرایی, کمدی
تاریخ انتشار: 1999
"گل دی. راجر" که به عنوان پادشاه دزدان دریایی شناخته می شد,قوی ترین و بدنام ترین دزد دریایی در دریایی گراند لاین است.دستگیر و اعدام او توسط دولت جهانی تغییراتی در دنیا به وجود می آورد.آخرین کلمات او قبل از مرگ مکان بزرگ ترین گنج دنیا به نام وان پیس را نشان میداد.این پیام شروع عصر دزدان دریایی بود,و مردانی که رویای پیدا کردن وان پیس(که وعده مقدار نامحدودی از ثروت و شهرت داده شده),که چیزی که هر کسی آرزوی به دست آوردن آن را داشت,لقب پادشاه دزدان دریایی."""
url_zer3 = "https://animesp.xyz/anime/1224#"
url_don3 ="https://dl4.animesp.xyz/Still%20Airing/One%20piece/720/"

suggested_dict = {"img": [img1, img2, img3], "cap": [cap1, cap2, cap3],
                  "url_zer": [url_zer1, url_zer2, url_zer3], "url_don": [url_don1, url_don2, url_don3]}

# _______ button anime suggested ______
def keyboard_suggested(url_sub, url_dow):
    keyboard = [
        [InlineKeyboardButton(text="زیر نویس", url=url_sub),
         InlineKeyboardButton(text="لینک دانلود", url=url_dow)],
        [InlineKeyboardButton(text="بعدی➡️", callback_data="suggested anime")]]

    suggested = InlineKeyboardMarkup(keyboard)
    return suggested


# _____keyboard start ________
def keyboard_start():
    keyboard = [[InlineKeyboardButton(text="جست و جو🔎", callback_data="name anime"),
                InlineKeyboardButton(text="انیمه پیشنهادی🏻", callback_data="suggested anime")],
                [InlineKeyboardButton(text="جدیدترین انیمه ها🌟", callback_data="new"),
                InlineKeyboardButton(text=f"تصویر زمینه🌃", callback_data="wallpaper")]]
    reply_start = InlineKeyboardMarkup(keyboard)
    return reply_start


#   ______keyboard code ________
def code(number: int):
    call_back = 0
    call_back2 = 1
    list_code = []
    for i in range(0, number, 2):
        punch: list =[InlineKeyboardButton(text=f"📥{i+1}", callback_data=call_back),
                      InlineKeyboardButton(text=f"📥{i+2}", callback_data=call_back2)]
        list_code.append(punch)
        call_back += 2
        call_back2 += 2
    reply_code = InlineKeyboardMarkup(list_code)
    return reply_code

# _______keyboard new anime______
def keyboard_new(url_sub, url_dow):
    keyboard = [
        [InlineKeyboardButton(text="زیر نویس", url=url_sub),
         InlineKeyboardButton(text="لینک دانلود", url=url_dow)]]

    new = InlineKeyboardMarkup(keyboard)
    return new
# ____text help_________
help_text="""
ربات انیمه بات برای دسترسی راحت تر شما به انیمه های هستش\n\n
✅در قسمت استارت شما میتونید با انتخاب گزینه (جست و جو🔎)انیمه خود را جست و جو کنید \n\n
✅در قسمت (جدیدترین انیمه ها🌟)می تونید به جدید فصل های انیمه که در سایت قرار گرفت دسترسی چیدا کنید\n\n
✅با انتخاب گزینه (انیمه پیشنهادی🤌🏻) انیمه با توضیحات مختصر درباره آن برای شما نمایش داده می شود \n\n
✅(تصویر زمینه🌃) مجموعه از والپیپر های از انیمه های مختلف وجود دارد که با هر بار فشار یک انیمه جدید نمایش داده می شود.
"""

import gspread
import pandas
sa = gspread.service_account(filename=".selnium/animest-424206-f150a87d1e25.json")
sh = sa.open("Animesp_API")
def glinks(list_link):
    # Add links to google sheet
    wks = sh.worksheet("link")
    wks.append_rows([list_link])

def guser(user_list):
    wks = sh.worksheet("account")
    wks.append_rows([user_list])
def gcheck(user, password):
    str(password)
    wks = sh.worksheet("account")
    df = pandas.DataFrame(wks.get_all_records(), dtype=object)
    df['password'] = df['password'].astype(str)
    if password in df['password'].values and user in df['username'].values:
        return True
    else:
        return False
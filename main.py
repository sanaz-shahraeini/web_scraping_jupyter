import time
from Anime_scrap_web import *
import anime_gsheet as ag

# First, you must register on the site. Site address: https://animesp.xyz/login
#
while True:
    Question = input("Do you have account?(yes/no): ").lower()
    if Question == "yes":
        break
    elif Question == "no":
        user_lis = [input("enter your name:  "), input("enter a password: "),
                    input("enter a username:  ")]
        ag.guser(user_lis)
        time.sleep(4)
        break
    else:
        continue
while True:
    # Enter username to test from:  zamir
    username = input("Enter your Username:  ")
    # Enter password to test from:  z@mir2000
    password = input("Enter your password:  ")
    check = ag.gcheck(username, password)
    if check is True:
        login("zamir", "z@mir2000")
        break
    else:
        print("The username or password is incorrect. Please try again")
        continue

while True:
    time.sleep(4)
    # Enter the name of the desired anime
    # Note: You must enter the space between letters with only one space
    name_anime = input("Enter Anime name(if To exit, write the 'exit'):  ").lower()
    if name_anime == "exit":
        break
    else:
        while True:
            result_page = search_(name_anime)
            dic_result = cards(result_page)
            try:
                number_result = len(dic_result["name"])
            except TypeError:
                print("The desired anime was not found. Please be careful in writing the name")
                continue
            print(f"The following anime list was found for you.\n"
                  f"Submit the anime code to get the download link")
            print()

            for i in range(number_result):
                result = dic_result["name"][i]
                print(f"code{i+1}: {result}")
            break

        # Send the code number of the anime you want
        while True:
            try:
                code_anime = int(input("Enter code Anime (just enter number): "))
                url_anime = dic_result["href"][code_anime-1]
            except IndexError:
                print("Choose from a range of code")
                continue
            except ValueError:
                print("choose just number")
                continue
            list_link = download(url_anime)
            print()
            break
    anime_data = [result]
    for j in list_link:
        anime_data.append(j)
    ag.glinks(anime_data)



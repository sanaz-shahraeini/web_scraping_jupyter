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
        print("___________log up_____________")
        user_lis = [str(input("enter your name:  ")), str(input("enter a password: ")),
                    str(input("enter a username:  "))]
        ag.guser(user_lis)
        time.sleep(4)
        break
    else:
        continue
i = 1
while True:
    print("___________log in_________")
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
        i += 1
        if i == 4:
            print("___________log up_____________")
            user_lis = [str(input("enter your name:  ")), str(input("enter a password: ")),
                        str(input("enter a username:  "))]
            ag.guser(user_lis)
            time.sleep(4)
            continue

while True:
    time.sleep(4)
    # Enter the name of the desired anime
    # Note: You must enter the space between letters with only one space
    print("___________search_________")
    name_anime = input("Enter Anime name(if To exit, write the 'exit'):  ").lower()
    if name_anime == "exit":
        break
    else:
        result_page = search_(name_anime)
        dic_result = cards(result_page)
        number_result = len(dic_result["name"])
        if number_result == 0:
            print("The desired anime was not found. Please be careful in writing the name")
            continue
        print()
        print(f"The following anime list was found for you.\n"
              f"Submit the anime code to get the download link")

        for i in range(number_result):
            result = dic_result["name"][i]
            print(f"code{i+1}: {result}")

    # Send the code number of the anime you want
    while True:
        try:
            code_anime = int(input("Enter code Anime (just enter number): "))
            if code_anime == 0:
                print("Choose from a range of code")
                continue
            else:
                code_anime -= 1
                url_anime = dic_result["href"][code_anime]
                break
        except IndexError:
            print("Choose from a range of code")
            continue
        except ValueError:
            print("choose just number")
            continue
    list_link = download(url_anime)
    anime_data = []
    for j in list_link:
        anime_data.append(j)
    ag.glinks(anime_data)
    print("______send links_______")
    print(anime_data)
    continue
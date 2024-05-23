from Anime_scrap import *

# First, you must register on the site. Site address: https://animesp.xyz/login

# Enter username to test from:  zamir
username = input("Enter your Username:  ")
# Enter password to test from:  z@mir2000
password = input("Enter your password:  ")
login(username, password)

# Enter the name of the desired anime
# Note: You must enter the space between letters with only one space
name_anime = input("Enter Anime name:  ")
result_page = search_(name_anime)
dic_result =cards(result_page)

print(f"The following anime list was found for you.\n"
      f"Submit the anime code to get the download link")
print()
number_result = len(dic_result["name"])
for i in range(number_result):
    result = dic_result["name"][i]
    print(f"code{i+1}: {result}")

# Send the code number of the anime you want
code_anime = int(input("Enter code Anime (just enter number): "))
url_anime = dic_result["href"][code_anime-1]
list_link = download(url_anime)
print()
print(f"Play online: {list_link[0]}\n"
      f"link download 720: {list_link[1]}\n"
      f"Subtitle: {list_link[2]}")
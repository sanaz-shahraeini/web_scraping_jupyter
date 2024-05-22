import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
driver.get("https://animesp.xyz/")
search = driver.find_element(By.XPATH, "//*[@id='header__form']")


def search_(text: object) -> object:
    """

    :type text: object
    """
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "header__form-input").click()
    textBox = driver.find_element(By.TAG_NAME, 'input')
    textBox.send_keys(text)
    textBox.send_keys(Keys.ENTER)
    url_anime = f"https://animesp.xyz/animes/search?title={text}".replace(" ", '+')
    return url_anime


def cards(url_cards):
    here_card = {'href': [], 'name': [], 'image': []}
    driver.get(url_cards)
    card_title = driver.find_elements(By.CLASS_NAME, "card__title")
    for card_anime in card_title:
        anime_title = card_anime.find_element(By.TAG_NAME, "a")
        here_card['href'].append(anime_title.get_attribute("href"))
        here_card['name'].append(anime_title.get_attribute('text'))
    card_cover = driver.find_elements(By.CLASS_NAME, "card__cover")
    for image in card_cover:
        imag = image.find_element(By.TAG_NAME, "img")
        here_card["image"].append(imag.get_attribute("src"))
    return here_card


def download(url_don):
    driver.get(url_don)
    link = driver.find_element(By.ID, 'download-links')
    mov_link = link.find_element(By.XPATH,
                                 "/html/body/section[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/a[2]")
    mov_link.click()
    #if new_url == "https://animesp.xyz/login":
        
name_anime = input("enter anime:  ")
test = search_(name_anime)
test2 = cards(test)
print(test2)
i = int(input("enter ur number of list:"))
download(test2['href'][i-1])

print("running")

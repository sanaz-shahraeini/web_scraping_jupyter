import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# If you don't want to use the graphic environment, use the following codes:
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver = webdriver.Firefox(options=options)

url = "https://animesp.xyz/login"
driver = webdriver.Firefox()
driver.get(url)

def login(user, user_pass):
    # login to site
    # The username and password are already created
    # you can create an account inside the site
    user_name = driver.find_element(By.ID, "username")
    user_name.click()
    user_name.send_keys(user)
    userpass = driver.find_element(By.ID, "password")
    userpass.click()
    userpass.send_keys(user_pass)
    button = driver. find_element(By.ID, "btn-submit")
    button.click()
    time.sleep(8)
def search_(text):
    # Search function on the site
    # Subject type input where each word must be written with a space
    search = driver.find_element(By.ID, "header__form")
    time.sleep(4)
    textBox = search.find_element(By.CLASS_NAME, 'header__form-input')
    textBox.click()
    textBox.send_keys(text)
    textBox.send_keys(Keys.ENTER)
    url_anime = f"https://animesp.xyz/animes/search?title={text}".replace(" ", '+')
    time.sleep(8)
    return url_anime


def cards(url_cards):
    # Scrap,Name and download page link of found items
    here_card = {'href': [], 'name': []}
    driver.get(url_cards)
    card_title = driver.find_elements(By.CLASS_NAME, "card__title")
    for card_anime in card_title:
        anime_title = card_anime.find_element(By.TAG_NAME, "a")
        here_card['href'].append(anime_title.get_attribute("href"))
        here_card['name'].append(anime_title.get_attribute('text'))
    time.sleep(8)
    return here_card


def download(url_don):
    # Scrap all the information to download the movie
    driver.get(url_don)
    down_link = driver.find_element(By.ID, 'download-links')
    list_links = down_link.find_elements(By.TAG_NAME,"a")
    link = []
    for href in list_links:
        link.append(href.get_attribute("href"))
    return link



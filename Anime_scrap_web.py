from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from random import choice

# If you don't want to use the graphic environment, use the following codes:
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()
url = "https://animesp.xyz/login"
driver.get(url)


def login(user, u_pass):
    # login to site
    # The username and password are already created
    # you can create an account inside the site
    user_name = driver.find_element(By.ID, "username")
    user_name.click()
    user_name.send_keys(user)
    user_pass = driver.find_element(By.ID, "password")
    user_pass.click()
    user_pass.send_keys(u_pass)
    button = driver.find_element(By.ID, "btn-submit")
    button.click()
    sleep(2)


def search_(text):
    # Search function on the site
    # Subject type input where each word must be written with a space
    search = driver.find_element(By.ID, "header__form")
    sleep(2)
    text_box = search.find_element(By.CLASS_NAME, 'header__form-input')
    text_box.click()
    text_box.send_keys(text)
    text_box.send_keys(Keys.ENTER)
    url_anime = f"https://animesp.xyz/animes/search?title={text}".replace(" ", '+')
    sleep(2)
    return url_anime


def cards(url_cards):
    # Scrap,Name and download page link of found items
    here_card = {'href': [], 'name': [], 'image': []}
    driver.get(url_cards)
    card_ = driver.find_elements(By.CLASS_NAME, "card")
    for card_anime in card_:
        anime_title = card_anime.find_element(By.TAG_NAME, "a")
        here_card['href'].append(anime_title.get_attribute("href"))
        src = card_anime.find_element(By.TAG_NAME, "img")
        here_card['image'].append(src.get_attribute("src"))
        here_card['name'].append(src.get_attribute("alt"))
    sleep(2)
    return here_card


def download(url_don):
    # Scrap all the information to download the movie
    driver.get(url_don)
    down_link = driver.find_element(By.ID, 'download-links')
    list_links = down_link.find_elements(By.TAG_NAME, "a")
    link = []
    for href in list_links:
        link.append(href.get_attribute("href"))
    return link
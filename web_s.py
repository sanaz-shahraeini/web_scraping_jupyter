import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=options)

driver.get("""https://animesp.xyz/""")
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
    url = f"https://animesp.xyz/animes/search?title={text}".replace(" ", '+')
    return url_anime

def cards(url):
    here_card = {'href': [], 'name': [], 'image': []}
    driver.get(url)
    card_title = driver.find_elements(By.CLASS_NAME,"card__title")
    for card_anime in card_title:
        anime_title = card_anime.find_element(By.TAG_NAME, "a")
        here_card['href'].append(anime_title.get_attribute("href"))
        here_card['name'].append(anime_title.get_attribute('text'))
    card_cover = driver.find_elements(By.CLASS_NAME, "card__cover")
    for image in card_cover:
        imag = image.find_element(By.TAG_NAME, "img")
        here_card["image"].append(imag.get_attribute("src"))
    return here_card

print("running")






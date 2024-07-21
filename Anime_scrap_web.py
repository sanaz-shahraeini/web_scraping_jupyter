from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

start = time.time()

# If you don't want to use the graphic environment, use the following codes:
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(options=options)
driver2 = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()
# driver2 = webdriver.Firefox()
url = "https://animesp.xyz/login"
url2 = "https://www.zoomg.ir/anime/"
driver.get(url)
driver2.get(url2)


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


def search_(text):
    # Search function on the site
    # Subject type input where each word must be written with a space
    search = driver.find_element(By.ID, "header__form")
    text_box = search.find_element(By.CLASS_NAME, 'header__form-input')
    text_box.click()
    text_box.send_keys(text)
    text_box.send_keys(Keys.ENTER)
    url_anime = f"https://animesp.xyz/animes/search?title={text}".replace(" ", '+')
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


def new_anime():
    sleep(4)
    global best, img, title, active
    driver.find_element(By.CLASS_NAME, "header__nav-link").click()
    dict_best = {"img": [], "title": []}
    best, img, title = [], [], []
    best_cards = driver.find_element(By.CLASS_NAME, "section,section--pb0")
    active = best_cards.find_elements(By.CLASS_NAME, "owl-item,active")
    for card in active:
        best.append(card.find_element(By.CLASS_NAME, "card"))
    for title_img in best:
        img.append(title_img.find_element(By.TAG_NAME, "a"))
        title.append(title_img.find_element(By.TAG_NAME, "h3"))
    for link_img in img:
        tag = link_img.find_element(By.CLASS_NAME, "lazy-images")
        dict_best["img"].append(tag.get_attribute("src"))
    for name_anime in title:
        name = name_anime.find_element(By.TAG_NAME, "a")
        dict_best["title"].append(name.get_attribute("text"))
    return dict_best


def news():
    anews = {"caption": [], "link": []}
    sleep(4)
    rows_news = driver2.find_elements(By.CLASS_NAME,
                                      "boxWrapper,latestArticles")
    for images in rows_news:
        srcs = images.find_element(By.CLASS_NAME, "imgContainer")
        tag_caption = srcs.find_element(By.CLASS_NAME,
                                        "Contents,col-md-8,col-sm-8,col-xs-8")
        link_news = tag_caption.find_element(By.TAG_NAME, "h3")
        link_news = link_news.find_element(By.TAG_NAME, "a")
        anews["link"].append(link_news.get_attribute("href"))
        anews["caption"].append(link_news.get_attribute("text"))
    driver2.close()
    return anews
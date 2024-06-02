
from bs4 import BeautifulSoup as BS
import pandas
data_book = {"name_books":[], "price_books":[], "star_books":[], "url_books":[]}
def scrape(url):
    soup = BS(url.text, 'html.parser')
    name_books= soup.find_all('h3')
    for name_book in name_books:
        names=name_book.a.get('title')
        data_book["name_books"].append(names)
    price_books = soup.find_all('p', class_='price_color')
    for price_book in price_books:
        data_book["price_books"].append(price_book.text)
    star_books = soup.find_all('article', class_="product_pod")
    for star_book in star_books:
        lis_star = list(star_book.p.get('class'))
        data_book["star_books"].append(lis_star[1])
    url_ = 'https://books.toscrape.com/'
    url_books = soup.find_all('h3')
    for url_book in url_books:
        url_book = url_ + url_book.a.get('href')
        data_book["url_books"].append(url_book)
    df_books = pandas.DataFrame(data=data_book)

    return df_books

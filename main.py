import requests
import pprint
from bs4 import BeautifulSoup

URL = "https://www.spiegel.de/schlagzeilen/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

articles = []

articles_cards = soup.find_all("div", {"data-area": "article_teaser>news-s-wide"})
for article in articles_cards:
    #print(article)
    title = article.find("span", {"class": "mr-6"}).text
    link = article.find("a")["href"]
    articles.append({"title": title, "link": link})
pprint.pprint(articles)
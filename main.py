import requests
from bs4 import BeautifulSoup

URL = "https://www.spiegel.de/schlagzeilen/"
page = requests.get(URL)
#print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
#data-area="article_teaser>news-s-wide"
articles_cards = soup.find_all("div", {"data-area": "article_teaser>news-s-wide"})
for article in articles_cards:
    #print(article)
    title = article.find("span", {"class": "mr-6"}).text
    link = article.find("a")["href"]
    print(title)
    print(link)
#print(results.prettify())
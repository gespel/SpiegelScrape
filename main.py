import requests
import pprint
import json
from termcolor import colored
from bs4 import BeautifulSoup
import datetime
from pathlib import Path
import time
import os
import logging

class SpiegelScrape:
    def __init__(self, filename):
        self.URL = "https://www.spiegel.de/schlagzeilen/"
        self.articles = []
        self.filename = filename
        logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s]: %(message)s', level=logging.INFO)
        self.logger = logging.getLogger("SpiegelScrape")
        self.logger.setLevel(logging.INFO)


    def scrape(self):
        page = requests.get(self.URL)

        soup = BeautifulSoup(page.content, "html.parser")

        articles = []

        articles_cards = soup.find_all("div", {"data-area": "article_teaser>news-s-wide"})
        for article in articles_cards:
            #print(article)
            title = article.find("span", {"class": "mr-6"}).text
            link = article.find("a")["href"]
            articles.append({"title": title, "link": link})

        #for article in articles:
        #    print(colored(article["title"], "green"))
        #    print(colored(article["link"], "magenta"))

        self.articles = articles

    def save_to_json(self):
        new = {
            "timestamp": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            "articles": self.articles
        }

        if Path(self.filename).is_file():
            with open(self.filename, "r") as f:
                old = json.loads(f.read())
            os.remove(self.filename)
        else:
            with open(self.filename, "w") as f:
                old = {
                    "data": []
                }

        with open(self.filename, "w") as f:
            old["data"].append(new)
            f.write(json.dumps(old))

    def scrape_loop(self, sleep_time):
        while True:
            self.scrape()
            self.save_to_json()
            self.logger.info("Scraping finished")
            time.sleep(sleep_time)

        
sp = SpiegelScrape("article_index.json")
sp.scrape_loop(10)
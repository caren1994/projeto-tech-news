import requests
from bs4 import BeautifulSoup
import time

HEADERS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    try:
        # recurso demora muito a responder
        time.sleep(1)
        response = requests.get(url, headers=HEADERS, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    url_news = []
    soup = BeautifulSoup(html_content, "html.parser")
    # vai codificar o html_content do jeito que ele precisa
    news = soup.find_all("article", class_="entry-preview")
    for new in news:
        url_news.append(new.find("a").get("href"))
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    father = soup.find("navigator", class_="navigation pagination")
    print(father)
    children = father.find("a", class_="next page-numbers").get("href")
    print(children)
    if children:
        return children
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

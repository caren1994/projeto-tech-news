import requests
from bs4 import BeautifulSoup
# from parsel import Selector
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
    # father = soup.find("nav", class_="navigation pagination")
    # print(father)
    children = soup.find("a", class_="next page-numbers")
    print(children)
    if children:
        return children.get("href")
    return None


# Requisito 4
def scrape_news(html_content):
    news = {}
    soup = BeautifulSoup(html_content, "html.parser")
    # selector = Selector(html_content)
    # selector para utilização do parsel
    h = soup.head
    news["url"] = h.find("link", {"rel": "canonical"}).get("href")
    news["title"] = soup.find("h1", class_="entry-title").text.strip()
    news["timestamp"] = soup.find("li", class_="meta-date").text
    news["writer"] = soup.find("span", class_="author").text
    news["reading_time"] = int(
        soup.find("li", class_="meta-reading-time").text.split(" ")[0]
    )
    news["summary"] = soup.find("div", class_="entry-content").p.text.strip()

    # news["summary"] = selector.xpath(
    #     "string(//div[@class='entry-content']/p[1])").get().strip()
    # // pega do nível inteiro para buscar a classe faz [@class=]
    # o / pega o filho e pegamos o primeiro p com p[1]

    # não sei fazer o reading-time e o sumary ver na instrução amanha
    news["category"] = soup.find("span", class_="label").text

    print(news)
    return news


#  get sempre tem que receber um parametro
# olhar keywordsarguments
# s.strip(): retorna a string resultante após a remoção do início
# e do final da string s de todos os caracteres em BRANCO;


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

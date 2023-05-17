from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# o parametro options i significa "case-insensitive"
# Requisito 8
def search_by_date(date):
    try:
        date_iso = datetime.strptime(date, "%Y-%m-%d")
        response = db.news.find({"timestamp": date_iso.strftime("%d/%m/%Y")})
    except Exception:
        raise ValueError("Data inválida")
    return [(new["title"], new["url"]) for new in response]


# Requisito 9
def search_by_category(category):
    response = db.news.find(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(new["title"], new["url"]) for new in response]

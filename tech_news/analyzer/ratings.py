from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    response = search_news({})
    categories = [new["category"] for new in response]
    count = Counter(categories).most_common(5)
    print(count)
    sort = sorted(count, key=lambda x: (-x[1], x[0]))
    # print(sort)
    return [category[0] for category in sort]


# most_common() retorna uma lista dos principais 'n' elementos
# do mais comum ao menos comum, conforme especificado no parâmetro 'n'.
# key parametro opcional colocamos a função lambda e declaramos a chave
#  e a lógica da ordenação que queremos e ele faz o trabalho
# -x[1] decrescente
# +[0] ordem alfabética

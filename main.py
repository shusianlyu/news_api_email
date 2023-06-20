import requests

api_key = "c4e83caa65fc402eb43daaece5baf9d3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-20&sortBy=" \
      "publishedAt&apiKey=c4e83caa65fc402eb43daaece5baf9d3"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

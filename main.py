import requests
from send_email import send_email

topic = "tesla"
api_key = "c4e83caa65fc402eb43daaece5baf9d3"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-05-20&" \
      "sortBy=publishedAt&" \
      "apiKey=c4e83caa65fc402eb43daaece5baf9d3&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"]:
        body += "Subject: Today's news" \
                + "\n" + article["title"] + "\n" + \
                article["description"] + \
                "\n" + article["url"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)

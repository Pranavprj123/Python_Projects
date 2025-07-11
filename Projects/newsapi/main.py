import requests

query = input("What type of news are you interested in? ")
api = "f0122a5a59394f048d2a95ff50c74202"

url  = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-11&sortBy=publishedAt&apiKey={api}"



print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1,article["title"])
    print(index + 1,article["description"])
    print(index + 1,article["url"])
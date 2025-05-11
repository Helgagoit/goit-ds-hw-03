import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com/"

all_quotes = []
authors_data = {}
visited_authors = set()  

def get_author(author_url):
    res = requests.get(BASE_URL + author_url)
    soup = BeautifulSoup(res.text, "html.parser")
    fullname = soup.find("h3", class_="author-title").text.strip()
    born_date = soup.find("span", class_="author-born-date").text.strip()
    born_location = soup.find("span", class_="author-born-location").text.strip()
    description = soup.find("div", class_="author-description").text.strip()
    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }

def scrape_quotes():
    page = 1
    while True:
        url = f"{BASE_URL}/page/{page}/"
        res = requests.get(url)
        if res.status_code != 200:
            break
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            break
        for quote in quotes:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            all_quotes.append({
                "tags": tags,
                "author": author,
                "quote": text
            })

            author_link = quote.find("a")["href"]
            if author_link not in visited_authors:
                visited_authors.add(author_link)
                author_info = get_author(author_link)
                authors_data[author_info["fullname"]] = author_info
        page += 1

scrape_quotes()

# Збереження у файли
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(all_quotes, file, indent=2, ensure_ascii=False)

with open("authors.json", "w", encoding="utf-8") as file:
    json.dump(list(authors_data.values()), file, indent=2, ensure_ascii=False)

print("Дані збережено у quotes.json та authors.json")
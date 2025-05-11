import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mixanik:CJVhg28w2mHRkkmy@cluster0.tsdelbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.quotes_bd

# Імпорт авторів
with open("authors.json", "r", encoding="utf-8") as f:
    authors = json.load(f)
    db.authors.delete_many({})  
    db.authors.insert_many(authors)


# Імпорт цитат
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)
    db.quotes.delete_many({})
    db.quotes.insert_many(quotes)

print("Дані успішно імпортовано у MongoDB Atlas!")
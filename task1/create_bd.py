
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mixanik:CJVhg28w2mHRkkmy@cluster0.tsdelbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
db = client.go_cats

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Створення БД

db.cats.insert_many([
    {
        "name": "Kvus",
        "age": 2,
        "features": ["ходить в лоток", "дає себе гладити", "тигристий"],
    },
    {
        "name": "Murka",
        "age": 4,
        "features": ["ходить в лоток", "дає себе гладити", "чорна"],
    },
    {
        "name": "Murzik",
        "age": 3,
        "features": ["ходить в лоток", "не дає себе гладити", "чорний"],
    },
    {
        "name": "Barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }
])


















# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi


# def get_db():
#     try:
#         client = MongoClient("mongodb://localhost:27017/")
#         db = client["cat_database"]
#         return db
#     except errors.ConnectionFailure as e:
#         print(f"Не вдалося підключитися до MongoDB: {e}")
#         return None


# def create_cat(name, age, features):
#     db = get_db()
#     if db:
#         try:
#             cat = {
#                 "name": name,
#                 "age": age,
#                 "features": features
#             }
#             db.cats.insert_one(cat)
#             print("Кота додано успішно.")
#         except Exception as e:
#             print(f"Помилка при додаванні кота: {e}")


# def read_all_cats():
#     db = get_db()
#     if db:
#         try:
#             cats = db.cats.find()
#             for cat in cats:
#                 print(cat)
#         except Exception as e:
#             print(f"Помилка при зчитуванні: {e}")


# def read_cat_by_name(name):
#     db = get_db()
#     if db:
#         try:
#             cat = db.cats.find_one({"name": name})
#             if cat:
#                 print(cat)
#             else:
#                 print("Кота не знайдено.")
#         except Exception as e:
#             print(f"Помилка при пошуку: {e}")


# def update_cat_age(name, new_age):
#     db = get_db()
#     if db:
#         try:
#             result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
#             if result.modified_count:
#                 print("Вік кота оновлено.")
#             else:
#                 print("Кота не знайдено або вік не змінено.")
#         except Exception as e:
#             print(f"Помилка при оновленні віку: {e}")


# def add_feature(name, feature):
#     db = get_db()
#     if db:
#         try:
#             result = db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
#             if result.modified_count:
#                 print("Характеристику додано.")
#             else:
#                 print("Кота не знайдено або характеристика вже існує.")
#         except Exception as e:
#             print(f"Помилка при оновленні характеристик: {e}")


# def delete_cat_by_name(name):
#     db = get_db()
#     if db:
#         try:
#             result = db.cats.delete_one({"name": name})
#             if result.deleted_count:
#                 print("Кота видалено.")
#             else:
#                 print("Кота не знайдено.")
#         except Exception as e:
#             print(f"Помилка при видаленні кота: {e}")


# def delete_all_cats():
#     db = get_db()
#     if db:
#         try:
#             result = db.cats.delete_many({})
#             print(f"Видалено записів: {result.deleted_count}")
#         except Exception as e:
#             print(f"Помилка при видаленні всіх записів: {e}")


# if __name__ == "__main__":
#     # Приклад використання
#     create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
#     read_all_cats()
#     read_cat_by_name("Barsik")
#     update_cat_age("Barsik", 4)
#     add_feature("Barsik", "мурчить")
#     read_cat_by_name("Barsik")
#     delete_cat_by_name("Barsik")
#     delete_all_cats()
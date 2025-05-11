from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

uri = "mongodb+srv://mixanik:CJVhg28w2mHRkkmy@cluster0.tsdelbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.go_cats


# Додавання нового запису (Create)
def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = db.cats.insert_one(cat)
        print(f"Кота додано з _id: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")

# Виведення всіх записів про котів (Read)
def read_all_cats():
    try:
        cats = db.cats.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при зчитуванні колекції: {e}")

# Виведення інформації про кота (Read)
def read_cat_by_name(name):
    try:
        cat = db.cats.find_one({"name": name})
        if cat:
           print(cat)
        else:
            print("Кота з таким ім’ям не знайдено.")
    except Exception as e:
        print(f"Помилка при пошуку: {e}")

 # Оновити вік кота за ім'ям (Update)    
def update_age_for_cat(name, new_age):
    try:
        result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Вік оновлено.")
        else:
            print("Кота не знайдено або вік не змінився.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")

# Додати нову характеристику до списку features (Update)
def add_feature_for_cat(name, new_feature):
    try:
        result = db.cats.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count:
            print("Характеристику додано.")
        else:
            print("Кота не знайдено або така характеристика існує.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

# Видалення запису з колекції за ім'ям тварини (Delete)
def delete_cat_by_name(name):
    try:
        result = db.cats.delete_one({"name": name})
        if result.deleted_count:
            print("Кота видалено.")
        else:
            print("Кота не знайдено.")
    except Exception as e:
        print(f"Помилка при видаленні запису: {e}")

# Видалення всіх записів із колекції (Delete)
def delete_all_cats():
    try:
        result = db.cats.delete_many({})
        print(f"Видалені всі записи про котів: {result.deleted_count}")
    except Exception as e:
        print(f"Помилка при видаленні записів з колекції: {e}")

 # Тестування
def main():
    create_cat("Marsik", 4, ["ходить в лоток", "дає себе гладити", "сірий"])
    read_all_cats()
    read_cat_by_name("Pushok")
    update_age_for_cat("Marsik", 5)
    add_feature_for_cat("Marsik", "любить спати")
    #delete_cat_by_name("Marsik")
    #delete_all_cats()


if __name__=="__main__":
    main()
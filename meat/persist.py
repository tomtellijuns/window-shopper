from pymongo import MongoClient
from meat_shopper import crawl

client = MongoClient('db', 27017)
db = client.test # Default database in mongodb docker
meat = db.meat

count = 1
for page in range(1, 101):
    for product in crawl(page):
        data = {
            'name': product[0],
            'code': product[1]
        }
        meat.insert_one(data)
        print(str(count) + '. ' + product[0] + ' --> ' + product[1])
        count += 1

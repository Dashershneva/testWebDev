import pymongo

client = pymongo.MongoClient()
db = client.hello
db.world.find()
for document in db.world.find():
    print(document)

for document in db.world.find({"asd.qwe": 1}):
    print(document)

db.world.insert_one({"test": "wow", "hi": ""})

for document in db.world.find_one({"test": "wow"}):
    print(document)
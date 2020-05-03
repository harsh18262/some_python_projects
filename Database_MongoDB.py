# basic program to add and find data using mongodb
import pymongo
from pymongo import MongoClient

data = MongoClient()
db = data.hello_world
user = db.users
name = input("enter name")
age = input("enter age")
user1 = {"Name": name, "Age": int(age)}
user2 = {"Name": "abdd", "Age": 12}
user3 = {"Name": "hffhfh", "Age": 22}
user_id1 = user.insert_one(user1)
user_id2 = user.insert_one(user2)
user_id3 = user.insert_one(user3)

for i in user.find({"Name": "adbb"}):
    print(i)

import motor.motor_asyncio
import pymongo
import os

DB_NAME = os.environ.get("DB_NAME","raju")
DB_URL = os.environ.get("DB_URL","mongodb+srv://VC:VC@cluster0.zyphn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values

async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

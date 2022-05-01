import motor.motor_asyncio
import pymongo
import os

DB_NAME = os.environ.get("DB_NAME","raju")
DB_URL = os.environ.get("DB_URL","mongodb+srv://VC:VC@cluster0.zyphn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups

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

async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

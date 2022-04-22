import pymongo
import motor.motor_asyncio
from config import DB_URI


DB_NAME = os.environ.get("DB_NAME","cloud19")                              
mongo = pymongo.MongoClient(DB_URI)
db = mongo[DB_NAME]
dbcol = db["user"]
 

    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

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
     













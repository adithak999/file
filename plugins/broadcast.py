from pyrogram import Client ,filters
from database import getid
from config import ADMINS

@Bot.on_message(filters.command('broadcast') & filters.private & filters.user(ADMINS))
async def broadcast(client: Bot, message: Message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass

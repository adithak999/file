#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""● ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/ccfilestorebot>sᴘɪᴅᴇʀᴍᴀɴ</a>
● ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/adpsycho>ᴀᴅɪᴛʜ</a>
● ᴅᴇᴠ : <a href=https://t.me/mr_MKN>ᴍʀ.ᴍᴋɴ ᴛɢ</a>
● 𝙻𝙸𝙱𝚁𝙰𝚁ʏ: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
● 𝙻𝙰𝙽𝙶𝚄𝙰𝙶ᴇ: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
● 𝙱𝙾ᴛ 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙾𝙺𝚃𝙴𝚃𝙾 𝙲𝙻𝙾𝚄𝙳""",                           
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

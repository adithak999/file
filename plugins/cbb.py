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
            text = f"""✯ 𝙼𝚈 𝙽𝙰𝙼𝙴 : Fiel store bot
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href=https://t.me/adpsycho>𝙰𝙳𝙸𝚃𝙷</a>
✯ 𝙳𝙴𝚅 : <a href=https://t.me/mr_MKN>𝐌𝐫.𝐌𝐊𝐍 𝐓𝐆</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙾𝙺𝚃𝙴𝚃𝙾 𝙲𝙻𝙾𝚄𝙳""",                           
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

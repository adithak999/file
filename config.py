import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5350587359:AAEPL4UIY8oM-bBCsYiqZM4gNkYM4qYblVQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12858393"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a295383aca802e9a3cd01df1fefe2310")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001785260530"))

#Database 
DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://UI:UI@cluster0.zggdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1067513987"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001678056679"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1067513987").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>⚠️ ᴘʟᴇᴀsᴇ ғᴏʟʟᴏᴡ ᴛʜɪs ʀᴜʟᴇs ⚠️\n\nആദ്യം ᴊᴏɪɴ ɢʀᴏᴜᴘ എന്ന ബട്ടൺ ക്ലിക്ക് ചെയ്തു ഗ്രൂപ്പിൽ ജോയിൻ ചെയ്.. എന്നിട്ട് വീണ്ടു ബോട്ടിൽ വന്നിട്ട് ᴍᴇ ᴊᴏɪɴᴇᴅ എന്ന ബട്ടൺ ക്ലിക്ക് ചെയ്താൽ ഫയൽ കിട്ടുന്നതായിരിക്കും\n\nFɪʀsᴛ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴊᴏɪɴ ɢʀᴏᴜᴘ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ. ᴛʜᴇɴ ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴄʟɪᴄᴋ ᴏɴ ᴍᴇ ᴊᴏɪɴᴇᴅ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ...</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b><i>{filename}\n\n=========== • ✠ • ===========\n▫️ ɢʀᴏᴜᴘ : @film_housc\n▫️ ᴄʜᴀɴɴᴇʟ : @film_hous =========== • ✠ • ===========</i></b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") 

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

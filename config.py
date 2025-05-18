import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7273432607:AAGoN4Qv7SbFoCgKdK_8xpEMrtPBMvg3rsA")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29803966"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "58d51659fe8038960a3db77d6e2c4265")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002451809103"))

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "879520667"))

# Port
PORT = os.environ.get("PORT", "8122")

# Database URL
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Shortner:aloksingh@shortner.svh6f.mongodb.net/?retryWrites=true&w=majority")

# Database Name
DB_NAME = os.environ.get("DATABASE_NAME", "insta")

# Join Requests Database
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
JOIN_REQS_DB2 = environ.get("JOIN_REQS_DB2", DB_URI)

# Force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002564979892"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002371777817"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002326952308"))

# Bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝙸 𝙲𝚊𝚗 𝚂𝚝𝚘𝚛𝚎 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝚒𝚗 𝚂𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚗𝚍 𝚘𝚝𝚑𝚎𝚛 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝙵𝚛𝚘𝚖 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔....!Я бы лучше умер, чем жил бы без страсти...\n\n𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 @cultured_backup🔥</b>.")

# Admins list
try:
    ADMINS = [8002331168]
    for x in (os.environ.get("ADMINS", "8156548943 7208536222 7568605154 7568605154 7062003886 7196015252 ").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝚃𝚑𝚎𝚜𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</b>\n\n Извини, чувак, тебе нужно присоединиться к этим каналам.\n\n<b>𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙲𝚕𝚒𝚌𝚔 𝙱𝚕𝚘𝚠 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 поэтому, пожалуйста, нажмите ниже, чтобы присоединиться 🔥</b>")

# Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect content
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Disable channel button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝙰𝚟𝚘𝚒𝚍 𝙳𝚒𝚛𝚎𝚌𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜. Я работаю только на @cultured_backup "

# Append owner ID to admins
ADMINS.append(OWNER_ID)
ADMINS.append(8002331168)

# Log file name
LOG_FILE_NAME = "filesharingbot.txt"

# Logging configuration
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

# Set logging level for Pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Logger function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)



import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token from BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7542241757:")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your Database Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388"))

# Bot Owner Info
OWNER = os.environ.get("OWNER", "sewxiy")
OWNER_ID = int(os.environ.get("OWNER_ID", "7328629001"))

# Port
PORT = os.environ.get("PORT", "8030")

# **Updated MongoDB Connection**
DB_URI = "mongodb+srv://janhavisolankey:janhavisolankey@cluster0.0fr4g.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Auto-Delete Message Time (in seconds)
TIME = int(os.environ.get("TIME", "43200"))

# Force Subscribe Channel IDs
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Custom Start and Force Pictures
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

# Shortlink Configuration
TOKEN = True if os.environ.get('TOKEN', "True") == "True" else False
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")

# Verification Expiry Time
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600))
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/hwdownload/3")

# Help & About Messages
HELP_TXT = "<b>Bot Commands:</b>\n/start - Start the bot\n/about - About the bot\n/help - Get help"
ABOUT_TXT = "<b>Developed by:</b> <a href='https://t.me/THE_FUNKY_FOX'>FUNKYFOX</a>"

# Start Message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}, welcome to the bot!</b>")

# Admin List
ADMINS = [6376328008, 7328629001]

# Force Subscription Message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Join our channels to access files.</b>")

# Custom Caption
CUSTOM_CAPTION = os.environ.get("MAIN_CHANNEL", "<b>• BY @foxyverts</b>")

# Protect Content
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

# Disable Channel Button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Logging
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

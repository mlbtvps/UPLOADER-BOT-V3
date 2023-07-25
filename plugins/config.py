import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5776880887:AAELyyG2jUUbZXxkpUu6VKUakGd1IRUbKNo")

    API_ID = int(os.environ.get("API_ID", 15830858))

    API_HASH = os.environ.get("API_HASH", "2c015c994c57b312708fecc8a2a0f1a6")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001862133848")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = ""

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "fhkt")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001860694129))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "5468192421"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001862133848")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ttkv5bot")

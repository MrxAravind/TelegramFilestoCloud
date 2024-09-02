from dotenv import load_dotenv
import os

load_dotenv()


BOT_USE = os.getenv("BOT_USE")
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
PIXELDRAIN_APIKEY = os.getenv("PIXELDRAIN_APIKEY")
AUTH_USERS = [int(id) for id in os.getenv("AUTH_USERS").split()]
TOKEN = os.environ.get('TOKEN', '')
COMMUNITY_ID = os.environ.get('COMMUNITY_ID', '')
GROUP_ID = os.environ.get('GROUP_ID', '')
SHRTLINK_APIKEY = os.environ.get('SHRTLINK_APIKEY', '')
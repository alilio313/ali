from pyrogram import Client
from asBASE import asJSON

db = asJSON("as.json")
###


SUDORS = [232499688] # ايديات المطورين
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TG_BOT_TOKEN")
bot = Client("control",API_ID,API_HASH,bot_token=TOKEN,in_memory=True)
bot_id = TOKEN.split(":")[0]

#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
# variables
API_ID = 24490919
API_HASH = "d1b3b15126c47dd4cb491553ee1db910"
BOT_TOKEN = "6354397130:AAFCed0ol-7QpddRJ8zRWs-JJWaZx3XKkK4"
SESSION = "BQF1s6cAT1We76J_xvM9cauuSCenGLnQPVJVDuHtVdSksfrLIVhszIlmRybGG3Cajl-8PGFYBxjr7mevY9v09WZh9w9LNnbg2GXRVZX7k60x6C1_GK1C0Xxv9f6hWXB-kuxW13eOR9I_2sp7dJYA3UAYteWEkjWlp4G1EvvtE87z0cZMTY9H-5va8FEP5F0pypFI9zPwuUUOZECCVz16YZANrkzqb6V-qtgOM1aPuObml3Il4d6cYCqaL76tD6lq-CHZXW0xx3pf6NWRDbSBqqQ24r9KTae_d3aVi-rxmFFcuKjJYzHrNrLMn8ho5aMX0ldKEHSimGlWvNAON5r5LBqPNnSrGgAAAAF0xr8GAA"
FORCESUB = "devgagan"
AUTH = 5621114370

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

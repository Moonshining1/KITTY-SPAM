import logging

from telethon import TelegramClient

from os import getenv
from JARVIS.data import FRIDAY


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR JARVIS BOTS
API_ID = 21617223
API_HASH = "388250849e21811b497f2614fd4619f7"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "kittyxspam")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = getenv("BOT_TOKEN", default="7016854687:AAGEzPV8l-fKE7Cpz29jao4PH1PMdbnkFXY")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default="7374213609:AAFXIBwaMLeeCELP5J3NYZcRJhG1xod011Y")
BOT_TOKEN3 = getenv("BOT_TOKEN3", default="6507210376:AAFwQPAR39gitNfviTXTnnww8UO9ne_8mCY")
BOT_TOKEN4 = getenv("BOT_TOKEN4", default="7067262732:AAFV-1kyOv8LkpasWnAy8kBseGurF_dQbas")
BOT_TOKEN5 = getenv("BOT_TOKEN5", default="6405439861:AAHHy1vTwv2XYvJTbgN5YKbXY08IJy3bvyE")
BOT_TOKEN6 = getenv("BOT_TOKEN6", default="6656770758:AAFi3oLJkJ9w9-YppIm1Kid9R-HsvqRBmSM")
BOT_TOKEN7 = getenv("BOT_TOKEN7", default="6608285973:AAEAHK0fAqhiYAgWs0pQyVCXc2CFnJzXWqQ")
BOT_TOKEN8 = getenv("BOT_TOKEN8", default="7183164856:AAEeX8wqN-xJatG6Aoln5BEs0ULSsQbSDcg")
BOT_TOKEN9 = getenv("BOT_TOKEN9", default="7042004567:AAEqasDun5gJU_K1_UkFyerfokJzCsJtBSQ")
BOT_TOKEN10 = getenv("BOT_TOKEN10", default="7128348935:AAHRqtkMVmuUw-nTTB0LFUTokLDXLTfTrK8")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6723933089").split()))
for x in FRIDAY:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6723933089"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

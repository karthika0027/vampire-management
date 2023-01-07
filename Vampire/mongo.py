import asyncio
import sys
from motor import motor_asyncio
from pymongo.mongo_client import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Vampire import MONGO_DB_URI
from Vampire.confing import get_int_key, get_str_key


MONGO_PORT = 27017
MONGO_DB_URI = "mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGO_DB = "Vampire"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["Vampire"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))

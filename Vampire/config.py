# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Vampire/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
    ALLOW_CHATS = None
    API_ID = 17713634  # integer value, dont use ""
    API_HASH = "a8c943a69022fef3ac66accc7ba8ce6b"
    TOKEN = "5924376156:AAEqYW9oQfWyx5DIOI8pLMrFkS4Q6sGgugs"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5432224567  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "the_team_vampire"
    SUPPORT_CHAT = "team_vampire_support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001770039008
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001770039008
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://logi_ifgz_user:Llhuylk1TRi0vnqjOVT16icrhlRrBQBL@dpg-cdpo6n1gp3jr9p5e11i0-a.singapore-postgres.render.com/logi_ifgz"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    MONGO_DB_URI= "mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY="UESBQW-LTTGOC-NHYELZ-LPXWOL-ARQ"
    ARQ_API_URL ="https://arq.hamker.in"
    TEMP_DOWNLOAD_DIRECTORY=None
    OPENWEATHERMAP_ID=None
    HEROKU_API_KEY=None
    HEROKU_APP_NAME=None
    REM_BG_API_KEY=None
    SESSION_STRING =None
    BOT_USERNAME="manage_x_bot"
    LASTFM_API_KEY=None
    CF_API_KEY=None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    BOT_ID=5924376156
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

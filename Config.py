import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "9688162"))
    API_HASH = os.environ.get("API_HASH", "7b2bd6db5aaf2fc6c21d08249189c028")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5621197727:AAGUdK7AErXR-j2UC-p_8RIa_euprsSNf2U")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Jamjamxmusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6435225"))

import os

API_ID = API_ID = 22779671

API_HASH = os.environ.get("API_HASH", "125d8d88b77309dc3b154cbbfc2dacb2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6152562853:AAGimPmtvHjqcE8em9iDMH-QAjkM8133P0c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1713924419))

LOG = -1002049391187

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1713924419").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

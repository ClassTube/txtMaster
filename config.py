import os

API_ID = API_ID = 27097807

API_HASH = os.environ.get("API_HASH", "9fd790a9cb1f639c921d941621d2959d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6351714036:AAFFameNDrmVv9fRHuLJ7r1mL0llIzx7NTM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1780080204))

LOG = -1002074844997

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1780080204").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

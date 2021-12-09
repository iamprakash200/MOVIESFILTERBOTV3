import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID','16080598'))
API_HASH = environ.get('API_HASH','c4c3748047d877b7aab584ffa301fbb5')
BOT_TOKEN = environ.get('BOT_TOKEN','5059689925:AAGO-3HtsCF2_eDWHfgtxuDZwM_m9C2_Rkk')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/4b39f2057c994a1869dc2.jpg https://telegra.ph/file/41223af455cf459191108.jpg https://telegra.ph/file/9a524407baf541572d8bc.jpg https://telegra.ph/file/d33e8953c66a7abda0df9.jpg https://telegra.ph/file/f6b77656c227c521aba74.jpg https://telegra.ph/file/18d8d581ac7bd170aeeae.jpg https://telegra.ph/file/a1868c88abca2d1d25a6e.jpg https://telegra.ph/file/378a2302e4801f9264b01.jpg https://telegra.ph/file/a35dbfda79ad2a7c46e43.jpg https://telegra.ph/file/b59ba12296f37b4bff4c7.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1396584367').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "-1001506954474").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1396584367').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL','-1001506954474')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1001515022008").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vkmoviesbot:vkmoviesbot@cluster0.fuxpb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "vkmoviesbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001528093646'))

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)

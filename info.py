import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7764533450').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/haxoffbot')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002500378345'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002356707323').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Aman")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Movies')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002500378345'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/4u6.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002500378345'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002562208871'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/haxoffverify/2")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/haxoffverify/2")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/haxoffverify/2")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://envs.sh/4CH.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "f1faba7501e855860c6a94bc0d24e7b11f1e4560")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "linkshortify.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "f1faba7501e855860c6a94bc0d24e7b11f1e4560")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "linkshortify.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "f1faba7501e855860c6a94bc0d24e7b11f1e4560")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "linkshortify.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "86400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "86400"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002548283647')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002394846437'))
SEARCH_GROUP = environ.get('SEARCH_GROUP', 'https://t.me/+XM9osWfyW7thMWVl')

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 120))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', True)

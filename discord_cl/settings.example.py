from .default_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Discord integration config
DISCORD_CLIENT_ID = ''
DISCORD_CLIENT_SECRET = ''
DISCORD_BOT_SECRET = ''
DISCORD_GUILD_ID = ''
DISCORD_REDIRECT_URI = 'http://127.0.0.1:8000/oauth/return'

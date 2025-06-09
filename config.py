import os

class Config(object):
####Dynamic Configs Variables####
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DB_NAME = os.environ.get("DB_NAME")
####Static Configs Variables####
    API_ID = 25318125 #API ID
    API_HASH = "b29fb6a928e8b8a3308f8c2d3ba9cfb0" #API HASH
    ADMIN_ID = 7764674199 #Admin ID
    DB_URL = "mongodb+srv://lucifer:QGPQCl6ZFf6wHiZ7@cluster0.zmcca.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #Database URL
    TXT_LOG = -1002844381920 #Text Log Channel ID
    LOG_CHANNEL = -1002654509383 #Log Channel ID
    CREDIT = "LUCIFER" #Credit
    PROXY = "103.172.85.194:50100" #Socks5 Proxy

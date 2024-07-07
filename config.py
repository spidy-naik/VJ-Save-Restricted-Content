import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7243457121:AAGrYohBljhlDZVfsKj8hJXTlby7-nrwojk")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25412293"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d58456be9931f3f6b8154a626fc1b3c6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ruhani:iwC9EVMuenUdA4qY@ruhani.u8a2fhl.mongodb.net/?retryWrites=true&w=majority")

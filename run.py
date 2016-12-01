from app import Bot
from os import environ

pairs = {}

pairs["[kK]nock[, -]*[kK]nock"] = "Who's there?"
pairs["help"] = "YOUR INSTRUCTIONS HERE"


pope_bot = Bot(environ['API_TOKEN'], pairs)
pope_bot.run()

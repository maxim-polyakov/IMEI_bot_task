import flask
from multiprocessing import Process
from Front_layer.telegram_bot import *
from aiogram import Bot, Dispatcher, executor
from Core_layer.Bot_package.Classes.Token import Token


tkn = Token.Token()
df = tkn.get_token('select token from assistant_sets.tokens where botname = \'Imei\' and platformname = \'Telegram\'')
API_TOKEN = df['token'][0]
#API_TOKEN = "7069527640:AAHNppnEcgguuRAo5CTBOhx30AlOoVm0Ycs"
boto = Bot(token=API_TOKEN)
app = flask.Flask(__name__)
dp = Dispatcher(bot=boto)

def bot_start_polling():
    executor.start_polling(dispatcher=dp, skip_updates=True)

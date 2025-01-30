from Front_layer import telegram_bot
from Core_layer.Bot_package.Classes.Imei import Imei


@telegram_bot.dp.message_handler(commands=['imei'])
async def get_user_text(message):
#
#
    input = message.text.replace('/imei ', '')
    found = Imei.Imei(text=input)
    res = found.get_imei()
    await telegram_bot.boto.send_message(message.chat.id, res)


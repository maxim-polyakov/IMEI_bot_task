import Front_layer.telegram_bot as tb
from Front_layer.telegram_bot import imei

# _______________________________________________________________________________
if __name__ == "__main__":
#
#
    bot_process = tb.Process(target=tb.bot_start_polling)
    bot_process.start()
    tb.app.run(host = '127.0.0.1', port='9000')



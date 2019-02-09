import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from simple_settings import settings


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n',
                    level=logging.INFO,
                    filename=settings.logfile)


def logger(func):
    def wrapper(bot, update):
        text = update.message.text
        user = update.message.from_user
        user = user.first_name + ' ' + user.last_name
        info = text + '\n' + user
        logging.info(info)
        func(bot, update)
    return wrapper


@logger
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm a bot, please talk to me!")


@logger
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


updater = Updater(settings.token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

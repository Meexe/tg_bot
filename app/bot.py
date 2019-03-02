import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from simple_settings import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n',
                    level=logging.INFO,
                    filename=settings.logfile)

start_text = "Привет! Я тот, кто будет водить. Собери всех участников в чатик и пригласи меня туда. Когда все будут готовы просто напишите /start_quest"


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
                     text='Привет, пригласи меня в чатик твоей команды...')


next_response = 'Next Quest Started /answer'
answer_response = 'Good job! /start'
tip_response = 'Here is your tip /next'

@logger
def next_quest(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=next_response)

@logger
def check_answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=answer_response)

@logger
def get_tip(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=tip_response)

updater = Updater(settings.token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
answer_handler = CommandHandler('answer', check_answer)
next_handler = CommandHandler('next', next_quest)
tip_handler = CommandHandler('tip', get_tip)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(next_handler)
dispatcher.add_handler(tip_handler)

updater.start_polling()


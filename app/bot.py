import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from simple_settings import settings
from time import sleep
from quest import Quest


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n',
                    level=logging.INFO,
                    filename=settings.logfile)


q = Quest()
chat_id = 0
start_text = "Привет! Я тот, кто будет вас водить по квесту. Собери всех участников в чатик и пригласи меня туда." \
             "Когда все будут готовы просто напишите /start_quest"


def logger(func):
    def wrapper(bot, update):
        text = update.message.text
        user = update.message.from_user
        user = user.first_name + ' ' + user.last_name
        info = text + '\n' + user
        logging.info(info)
        func(bot, update)
    return wrapper


def send_messages(bot, *messages):
    methods = {
        'voice': bot.send_voice,
        'photo': bot.send_photo,
        'text': bot.send_message,
        'doc': bot.send_document
    }

    for message in messages:
        func = methods[message['type']]
        func(chat_id, message['payload'])
        sleep(message['delay'])


@logger
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=start_text)


@logger
def start_quest(bot, update):
    chat_id = update.message.chat_id
    messages = q.start_task()
    send_messages(messages)


@logger
def next_quest(bot, update):
    messages = q.end_task() + q.start_task()
    send_messages(messages)


# @logger
# def get_tip(bot, update):
#     bot.send_message(chat_id=update.message.chat_id,
#                      text=tip_response)


updater = Updater(settings.token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
start_quest_handler = CommandHandler('start_quest', start_quest)
next_handler = CommandHandler('next', next_quest)
# tip_handler = CommandHandler('tip', get_tip)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_quest_handler)
dispatcher.add_handler(next_handler)
# dispatcher.add_handler(tip_handler)

updater.start_polling()

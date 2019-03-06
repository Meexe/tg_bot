import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from simple_settings import settings
from time import sleep
from quest import Quest

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n',
                    level=logging.INFO,
                    filename=settings.logfile)


q = Quest()
start_text = "Приветствую, я БотБегемот и в честь 8 марта я вас поведу на бал к мессиру Воланду!\n/start_quest"


def logger(func):
    def wrapper(bot, update, *args, **kwargs):
        chat_id = str(update.message.chat_id)
        text = str(update.message.text)
        user = update.message.from_user
        user = str(user.first_name) + ' ' + str(user.last_name)
        info = text + '\n' + user + '\n' + chat_id
        bot.forward_message(q.admin, chat_id, update.message.message_id)
        logging.info(info)
        func(bot, update, *args, **kwargs)
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
        func(q.chat_id, message['payload'])
        sleep(message['delay'])


@logger
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=start_text)


@logger
def start_quest(bot, update):
    q.chat_id = update.message.chat_id
    messages = q.start_task()
    send_messages(bot, *messages)


@logger
def next_quest(bot, update):
    messages = q.end_task() + q.start_task()
    send_messages(bot, *messages)


@logger
def get_tip(bot, update):
    pass


@logger
def give_tip(bot, update, args):
    message = " ".join(args)
    bot.send_message(q.chat_id, message)


@logger
def handle_input(bot, context):
    pass


updater = Updater(settings.token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
start_quest_handler = CommandHandler('start_quest', start_quest)
next_handler = CommandHandler('next', next_quest)
get_tip_handler = CommandHandler('tip', get_tip)
give_tip_handler = CommandHandler('give_tip', give_tip, pass_args=True)
input_handler = MessageHandler((~ Filters.command), handle_input)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_quest_handler)
dispatcher.add_handler(next_handler)
dispatcher.add_handler(get_tip_handler)
dispatcher.add_handler(give_tip_handler)
dispatcher.add_handler(input_handler)

updater.start_polling()

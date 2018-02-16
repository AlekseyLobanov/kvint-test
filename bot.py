# -*- coding: utf-8 -*-
import os
import time
import logging

import telebot

TELEGRAM_API_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)


def init_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y.%m.%d %H:%M:%S'
    )

if __name__ == '__main__':
    init_logging()
    logging.debug("Using token {}".format(TELEGRAM_API_TOKEN[-4:]))
    bot.polling(none_stop=True)

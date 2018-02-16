# -*- coding: utf-8 -*-

"""
Модуль взаимодействия с Telegram.
"""

import os
import time
import logging

import telebot

from core import dialog

TELEGRAM_API_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def process_msg(message):
    uid = "telegram_{}".format(message.chat.id)
    
    bot.send_message(
        message.chat.id,
        dialog.proc(uid, message.text)
    )


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

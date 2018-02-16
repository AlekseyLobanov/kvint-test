# -*- coding: utf-8 -*-
import os
import time

import telebot

TELEGRAM_API_TOKEN = os.environ['TELEGRAM_TOKEN']
print("Using token {}".format(TELEGRAM_API_TOKEN[-4:])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)

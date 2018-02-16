# -*- coding: utf-8 -*-
import os
import telebot

TELEGRAM_API_TOKEN = os.environ['TELEGRAM_TOKEN']
print("Using token {}".format(TELEGRAM_API_TOKEN[-4:])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:11:23 2021

@author: gian
"""

from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hola Humano')

if __name__ == '__main__':
    token= '1825585903:AAGrwQlo9G8uCjKCze62-EFmKIrZtJTIhcU'
    updater = Updater(token= token, use_context=True)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    
    updater.start_polling()
    updater.idle()
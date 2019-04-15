import telegram
from telegram.ext import Updater
from random import choice
import config


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = config.user_id
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def sendSticker(self):
        stickers = self.core.get_sticker_set('animals').stickers
        self.core.send_sticker(chat_id=self.id, sticker=choice(stickers))

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

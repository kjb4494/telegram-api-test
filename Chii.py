from TelegramBot import TelegramBot
from telegram.ext import CommandHandler
import config


class Chii(TelegramBot):
    def __init__(self):
        self.token = config.token
        TelegramBot.__init__(self, '치이', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('치이 봇이 잠에서 깨어납니다.')
        self.updater.start_polling()
        self.updater.idle()

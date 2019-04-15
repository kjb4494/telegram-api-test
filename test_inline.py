import logging
from uuid import uuid4
import telegram
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineQueryResultCachedSticker
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = config.token

core = telegram.Bot(token)
stickers = core.get_sticker_set('animals').stickers
all_sticker_list = []
for i in range(10):
    all_sticker_list.append(InlineQueryResultCachedSticker(
        id=uuid4(),
        sticker_file_id=stickers[i].file_id
    ))
sticker_dict = {
    'test1': all_sticker_list[0],
    'test2': all_sticker_list[1],
    'test3': all_sticker_list[2],
    'test4': all_sticker_list[3],
    'test5': all_sticker_list[4],
    'test6': all_sticker_list[5],
    'test7': all_sticker_list[6],
    'test8': all_sticker_list[7],
    'test9': all_sticker_list[8],
    'test10': all_sticker_list[9],
}

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.sendMessage(chat_id=config.user_id, text='Hi')
#
#
# def help(update, context):
#     """Send a message when the command /help is issued."""
#     update.sendMessage(chat_id=config.user_id, text='@ProtoTypeTestBot test1, test2, ... , test10')


def inlinequery(update, context):
    """Handle the inline query."""
    print(update)
    print(context)
    query = context.inline_query.query

    if sticker_dict.get(query) is None:
        context.inline_query.answer(all_sticker_list)
    else:
        context.inline_query.answer([sticker_dict.get(query)])


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

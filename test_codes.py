import telegram
from Chii import Chii


def test_code():
    chii_token = '842285928:AAFDNrPcHhUdMxc67AfJnWOyI0g9ucwX4zw'
    chii = telegram.Bot(token=chii_token)
    updates = chii.getUpdates()
    for u in updates:
        print(u.message)


def get_sticker(file_id):
    return telegram.Sticker(
        file_id=file_id,
        width='512',
        height='512'
    )


def proc_hello(bot, update):
    chii.sendMessage('안녕하...')
    chii.sendMessage('...살법!')


def proc_sticker_test(bot, update):
    chii.sendSticker()


def proc_rolling(bot, update):
    chii.sendMessage('데구르르...')
    chii.sendMessage('팡팡!')
    chii.sendMessage('르르...')


def proc_stop(bot, update):
    chii.sendMessage('치이가 잠듭니다.')
    chii.stop()


if __name__ == '__main__':
    # test_code()
    chii = Chii()
    chii.add_handler('hello', proc_hello)
    chii.add_handler('rolling', proc_rolling)
    chii.add_handler('stop', proc_stop)
    chii.add_handler('sticker_test', proc_sticker_test)
    chii.start()

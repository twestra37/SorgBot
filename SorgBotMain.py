from SorgBot import SorgBot

# noinspection SpellCheckingInspection
main_bot = SorgBot('525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY')
greetings = ('hello', 'hi')


def mainrun() -> None:
    new_offset = None

    while True:
        main_bot.get_updates(new_offset)

        last_update = main_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_text = last_update['message']['text']

        if last_chat_text.lower() in greetings:
            main_bot.send_message(last_chat_id, 'hey, bitch')
        new_offset = last_update_id + 1


if __name__ == "__main__":
    try:
        mainrun()
    except KeyboardInterrupt:
        exit()

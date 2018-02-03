import _random

class SorgBot:
    from SorgBot import SorgBot

    # noinspection SpellCheckingInspection
    main_bot = SorgBot('525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY')
    jokeKeyWord = 'Throw me a line'
    jokeList.add('Hi, I hear you\'re good at algebra.....Will you replace my eX without asking Y?')
    jokeList.add('I wish I was your derivative so I could lie tangent to your curves')
    jokeList.add('Are you a 90 degree angle? Cause you\'re looking right!')
    jokeList.add('Our love is like dividing by zero; its undefinable')
    jokeList.add('If I were a function, you\'d be my asymptote. I\'d always tend towards you')
    jokeList.add('Hunny, you\'re sweeter than pi')
    jokeList.add('You\'ve got more curves than a triple integral')
    jokeList.add('I\'ll be the student to you\'re math book. I\'ll solve all your problems')
    jokeList.add('You up?')


    def mainrun() -> None:
        new_offset = None

        while True:
            main_bot.get_updates(new_offset)

            last_update = main_bot.get_last_update()

            last_update_id = last_update['update_id']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_text = last_update['message']['text']

            if last_chat_text.lower() in jokeKeyWord:
                main_bot.send_message(last_chat_id, random.choice(jokeList))
            new_offset = last_update_id + 1

    if __name__ == "__main__":
        try:
            mainrun()
        except KeyboardInterrupt:
            exit()
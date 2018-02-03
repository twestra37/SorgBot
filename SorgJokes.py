import _random

class SorgBot:
    from SorgBot import SorgBot

    # noinspection SpellCheckingInspection
    main_bot = SorgBot('525519947:AAG2k1H8wZb_G01YEv-cIh0Tq0DCnQQYBKY')
    jokeKeyWord = 'tell me a joke'
    jokeList.add('What do you get if you divide the circumference of a jack-o-lantern by its diameter? Pumpkin Pi')
    jokeList.add('What did Al Gore play on his guitar? An algorithm')
    jokeList.add('What do you call dudes who love math? Algebros!')
    jokeList.add('With the Ark settled safely after the flood, Noah opens the doors and commands the animals, “Go forth and multiply!” All the animals depart the Ark, except for two snakes in the back. Noah proclaims again, “Go forth and multiply,” yet the snakes stay put. Perturbed, Noah finally asks them, “Why have you not followed my command?” The snakes flicker their tongues and answer, “We can’t multiply, Noah—we’re Adders.')
    jokeList.add('Old mathematicians never die, they just lose some of their functions')
    jokeList.add('Why did the mathematician divide sin by tan? Just cos')
    jokeList.add('60 out of 50 people have trouble with fractions')
    jokeList.add('Why is the obtuse triangle depressed? It is never right')
    jokeList.add('Your grade')
    jokeList.add('Your love life')

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

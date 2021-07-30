from typing import Tuple

from .words import WORDS


def get_game_mode() -> Tuple[int, str]:
    print('Hello & Welcome to translate words game!')
    print('Choose your game mode:')
    print('1. Practice with hints')
    print('2. Practice without hints')
    user_choice = input('Your mode is: ')

    print(f'Do you want to practice all words ({len(WORDS)} words) or some of it?\n'
          'Press Enter for all words, or insert how many words you wish to practice')
    words_count = input('Insert here:')

    return int(user_choice), words_count or str(len(WORDS))


def game_flow():
    user_choice, words_count = get_game_mode()
    print(f'user choice: {user_choice}, words count: {words_count}')

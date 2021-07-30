from random import choice
from typing import Tuple, Dict

from .words import WORDS


def get_game_mode() -> Tuple[int, int]:
    print('Hello & Welcome to translate words game!')
    print('Choose your game mode:')
    print('1. Practice with hints')
    print('2. Practice without hints')
    user_choice = input('Your mode is: ')

    print(f'Do you want to practice all words ({len(WORDS)} words) or some of it?\n'
          'Press Enter for all words, or insert how many words you wish to practice')
    words_count = input('Insert here:')

    return int(user_choice), int(words_count) or len(WORDS)


def get_random_words(words_count: int) -> Dict:
    """
    Get random chose words from words collection.
    """
    words_keys = list(WORDS)
    game_words = {}

    for _ in range(words_count):
        word = choice(words_keys)
        while word in game_words:
            word = choice(words_keys)

        if word not in game_words:
            game_words[word] = WORDS[word]

    assert len(game_words) == words_count
    return game_words


def play_game(game_mode: int, words_count: int) -> None:
    words_list = WORDS if words_count == len(WORDS) else get_random_words(words_count)
    print(words_list)


def game_flow():
    user_choice, words_count = get_game_mode()
    print(f'user choice: {user_choice}, words count: {words_count}')

    play_game(user_choice, words_count)

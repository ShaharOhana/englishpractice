from random import choice
from typing import Tuple, Dict, AnyStr, Union, List

from colorama import Fore

from .consts import GameMode
from .words import WORDS


def get_game_mode() -> Tuple[int, int]:
    print(Fore.CYAN + 'Hello & Welcome to translate words game!')
    print(Fore.WHITE + '\nChoose your game mode:')
    print('1. Practice with hints')
    print('2. Practice without hints')
    user_choice = input('Your mode is: ')

    print(f'\nDo you want to practice all words ({len(WORDS)} words) or some of it?\n'
          'Press Enter for all words, or insert how many words you wish to practice')
    words_count = input('Insert here:')

    return int(user_choice), int(words_count) or len(WORDS)


def get_random_words(words_count: int) -> Dict[AnyStr, Union[AnyStr, List[AnyStr]]]:
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


def play_game(game_mode: int, words_count: int) -> Dict[AnyStr, Dict[AnyStr, Union[AnyStr, List[AnyStr]]]]:
    words_list = WORDS if words_count == len(WORDS) else get_random_words(words_count)
    mistakes = {}

    print(Fore.CYAN + '\n~~~ LET\'S PLAY! ~~~')
    if game_mode == GameMode.WITH_HINTS:
        print(Fore.WHITE + 'Remember, if you need hint, enter (h) instead of answer')

    for word, translation in words_list.items():
        answer = input(Fore.WHITE + f'\n{word} is -> ')
        if answer == 'h':
            if game_mode == GameMode.WITH_HINTS:
                print(Fore.LIGHTYELLOW_EX + f'The answer is: {translation}')
            else:
                print(Fore.RED + 'YOU CANT USE HINTS (sorry...)')
                answer = input(Fore.WHITE + f'Try again: {word} is -> ')

        elif (isinstance(translation, list) and answer in translation) or \
                (isinstance(translation, str) and answer == translation):
            print(Fore.GREEN + 'Good Job!')
        else:
            print(Fore.WHITE + f'Don\'t worry, {word}\'s translation is: {translation}')
            mistakes[word] = {'user': answer, 'correct': translation}

    return mistakes


def game_flow():
    user_choice, words_count = get_game_mode()

    mistakes = play_game(user_choice, words_count)

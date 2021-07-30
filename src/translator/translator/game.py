from random import choice
from typing import Tuple, Dict, AnyStr, Union, List

from colorama import Fore

from .consts import GameMode, HINT_CHAR
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
        print(Fore.WHITE + f'Remember, if you need hint, enter ({HINT_CHAR}) instead of answer')

    for word, translation in words_list.items():
        answer = input(Fore.WHITE + f'\n{word} is -> ')
        if answer == HINT_CHAR:
            if game_mode == GameMode.WITH_HINTS:
                print(Fore.LIGHTYELLOW_EX + f'The answer is: {translation}')
                mistakes[word] = {'user': answer, 'correct': translation}
            else:
                print(Fore.RED + 'YOU CANT USE HINTS (sorry...)')
                answer = input(Fore.WHITE + f'Try again: {word} is -> ')

        if (isinstance(translation, list) and answer in translation) or \
                (isinstance(translation, str) and answer == translation):
            print(Fore.GREEN + 'Good Job!')
        elif answer != HINT_CHAR:
            print(Fore.WHITE + f'Don\'t worry, {word}\'s translation is: {translation}')
            mistakes[word] = {'user': answer, 'correct': translation}

    return mistakes


def summary(mistakes: Dict[AnyStr, Dict[AnyStr, Union[AnyStr, List[AnyStr]]]], words_count: int) -> None:
    print(Fore.CYAN + '\n~~~ GAME SUMMARY ~~~')
    print(Fore.CYAN + f'Your result is: {words_count - len(mistakes)}/{words_count}')

    if not mistakes:
        print(Fore.LIGHTGREEN_EX + 'Awesome!! You know all the words!')
    else:
        print(Fore.WHITE + 'Summary of your mistakes, and correct answers:')
        for word, answer in mistakes.items():
            print(f"{word}: your answer was - {answer['user']}, the correct answer is: {answer['correct']}")


def game_flow():
    user_choice, words_count = get_game_mode()
    assert user_choice in GameMode.values(), Fore.RED + 'Game choice is not valid'
    assert 1 <= words_count <= len(WORDS), Fore.RED + f'Invalid words count - should be between 1 to {len(WORDS)}'

    mistakes = play_game(user_choice, words_count)
    summary(mistakes, words_count)

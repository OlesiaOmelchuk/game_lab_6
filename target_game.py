"""Target game"""
from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters_list = []

    for i in range(9):
        letter_ord = random.randint(97, 122)
        letters_list.append(chr(letter_ord))

    return letters_list


def get_words(path: str, letters: List[str]) -> List[str]:
    """
    Reads the file path. Checks the words with rules and returns a list of words.
    """
    # letters_tuples = []
    # grid_list = []
    # for letter in letters_list:
    #     letters_tuples.append((letter, letters_list.count(letter)))
    # for letter in letters_tuples:
    #     if letter not in grid_list:
    #         grid_list.append(letter)
    words_from_dict = []

    with open(path, 'r') as file:
        content = file.read()
    content = content.lower()
    all_words = content.split()
    del all_words[0:4]

    central_letter = letters[4]
    for word in all_words:
        if (len(word) >= 4) and (word.count(central_letter) >= 1):
            num = 0
            for letter in word:
                if letters.count(letter) >= 1:
                    num += 1
            if num == len(word):
                num = 0
                for letter in word:
                    if word.count(letter) <= letters.count(letter):
                        num += 1
                if num == len(word):
                    words_from_dict.append(word)
    return words_from_dict

# print(get_words('/home/olesia/UCU_OP/Year_1/Lab_6/game_lab_6/en.txt', [el for el in 'jniarnoah']))


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    while True:
        try:
            user_words.append(input())
        except EOFError:
            return user_words


def get_pure_user_words(user_words: List[str], letters: List[str],\
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    central_letter = letters[4]
    for word in user_words:
        if (len(word) >= 4) and (word.count(central_letter) >= 1):
            num = 0
            for letter in word:
                if letters.count(letter) >= 1:
                    num += 1
            if num == len(word):
                num = 0
                for letter in word:
                    if word.count(letter) <= letters.count(letter):
                        num += 1
                if num == len(word):
                    if words_from_dict.count(word) == 0:
                        pure_words.append(word)
    return pure_words


def results():
    """
    Prints results of the game and writes them into a file result.txt
    """
    dict_words = get_words("en.txt", generate_grid())
    user_words = get_user_words()
    letters = generate_grid()
    pure_words = get_pure_user_words(user_words, letters, dict_words)

    print(len(user_words) - len(pure_words))
    print(dict_words)
    print(user_words)
    print(pure_words)

    with open('result.txt', 'w') as file:
        file.write(len(user_words) - len(pure_words), '\n',
                   dict_words, '\n', user_words, '\n', pure_words, '\n')

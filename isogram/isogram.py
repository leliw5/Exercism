import re


def is_isogram(string: str):
    letters = []
    for letter in re.sub('[ -]', "", string.lower()):
        if letter in letters:
            return False
        letters.append(letter)
    return True

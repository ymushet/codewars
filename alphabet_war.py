from typing import List

LEFT_ARMY = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 1}
#LEFT_ARMY = {'w': 4, 'p': 3, 'b': 2, 's': 1}

RIGHT_ARMY = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 3}
#RIGHT_ARMY = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

# We will consider 'y' not a vowel letter https://simple.wikipedia.org/wiki/Vowel
VOWEL_ARMY = {'a': 1, 'e': 1, 'i' : 1, 'o': 1, 'u': 1}
LEFT = { 'phrase': 'Left side wins!', 'army': LEFT_ARMY}
RIGHT = {'phrase': 'Right side wins!', 'army': RIGHT_ARMY}
VOWEL = {'phrase': 'Vowel side wins!', 'army': VOWEL_ARMY}
DEFAULT_PHRASE = 'Let\'s fight again!'
ARMY_LIST = [LEFT, RIGHT, VOWEL]
#ARMY_LIST = [LEFT, RIGHT]

def find_letters_values(letters: list, values : dict) -> int:
    res = 0
    for l in letters:
        if l in values.keys():
            res += values[l]
    return res

def find_winner(values : List[int]) -> str:
    max_value = max(values)
    if max_value == 0 or values.count(max_value) != 1:
        return DEFAULT_PHRASE

    index = values.index(max_value)
    army = ARMY_LIST[index]
    return army['phrase']

def alphabet_war(text : str) -> str:
    """
    >>> alphabet_war('')
    "Let's fight again!"
    >>> alphabet_war('abracadabra')
    'Vowel side wins!'
    >>> alphabet_war('z')
    'Right side wins!'
    >>> alphabet_war('zdqmwpbs')
    "Let's fight again!"
    >>> alphabet_war('zzzzs')
    'Right side wins!'
    >>> alphabet_war('wwwwwwz')
    'Left side wins!'
    >>> alphabet_war('u')
    'Vowel side wins!'
    >>> alphabet_war('aemmm')
    'Right side wins!'
    """

    letters = list(text)
    values_list = []
    for a in ARMY_LIST:
        values = find_letters_values(letters, a['army'])
        values_list.append(values)

    return find_winner(values_list)

if __name__ == "__main__":
    """
    See https://www.codewars.com/kata/alphabet-war
    """
    # python -m doctest alphabet_war.py
    print(alphabet_war('u'))

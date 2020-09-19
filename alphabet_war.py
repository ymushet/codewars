from typing import List

left_army = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 1}

right_army = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 3}

# We will consider 'y' not a vowel letter https://simple.wikipedia.org/wiki/Vowel
vowel_army = {'a': 1, 'e': 1, 'i' : 1, 'o': 1, 'u': 1}

left = { 'phrase': 'Left side wins!', 'army': left_army}

right = {'phrase': 'Right side wins!', 'army': right_army}

vowel = {'phrase': 'Vowel side wins!', 'army': vowel_army}

army_list = frozenset(left, right, vowel)

def find_letters_values(letters: list, values : dict) -> int:
    res = 0
    for l in letters:
        if l in values.keys():
            res += values[l]
    return res

def find_winner(values : List[int]) -> str:
    
    return 'Let\'s fight again!'

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
    for a in army_list:
        values = find_letters_values(letters,a['army'])
        values_list.append(values)

    return find_winner(values_list)

if __name__ == "__main__":
    """
    See https://www.codewars.com/kata/alphabet-war
    """
    # python -m doctest alphabet_war.py
    print(alphabet_war('u'))

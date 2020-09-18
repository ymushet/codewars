left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 1}
right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 3}
# We will consider 'y' not a vowel letter https://simple.wikipedia.org/wiki/Vowel
vowel_side = {'a': 1, 'e': 1, 'i' : 1, 'o': 1, 'u': 1}

def find_letters_values(letters: list, values : dict) -> int:
    res = 0
    for l in letters:
        if l in values.keys():
            res += values[l]
    return res

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
    right = find_letters_values(letters, right_side)
    left = find_letters_values(letters, left_side)
    vowel = find_letters_values(letters, vowel_side)
    if right > left and right > vowel:
        return 'Right side wins!'
    elif left > right and left > vowel:
        return 'Left side wins!'
    elif vowel > left and vowel > right:
        return 'Vowel side wins!'

    return 'Let\'s fight again!'

if __name__ == "__main__":
    """
    See https://www.codewars.com/kata/alphabet-war
    """
    # python -m doctest alphabet_war.py
    print(alphabet_war('u'))

left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
right_side = {'m': 4, 'q': 3, 'd': 1, 'z': 1}

def find_letters_values(letters: list, values : dict) -> int:
    res = 0
    for l in letters:
        if l in values.keys():
            res += values[l]
    return res

def fight(text : str) -> str:
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    """

    letters = list(text)
    index = int(len(letters) / 2)
    right = find_letters_values(letters[index:], right_side)
    left = find_letters_values(letters[:index], left_side)
    if right > left:
        return 'Right side wins!'
    elif left > right:
        return 'Left side wins!'
    return 'Let\'s fight again!'

if __name__ == "__main__":
    print(fight(''))
    print(fight('abracadabra'))
    print(fight('z'))
    print(fight('zdqmwpbs'))
    print(fight('zzzzs'))
    print(fight('wwwwwwz'))

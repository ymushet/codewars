left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

def find_letters_values(letters: list, values : dict) -> int:
    res = 0
    for l in letters:
        if l in values.keys():
            res += values[l]
    return res

def alphabet_war(text : str) -> str:
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
    right = find_letters_values(letters, right_side)
    left = find_letters_values(letters, left_side)
    if right > left:
        return 'Right side wins!'
    elif left > right:
        return 'Left side wins!'
    print(left, right)
    return 'Let\'s fight again!'

if __name__ == "__main__":
    """
    See https://www.codewars.com/kata/alphabet-war
    """
    print(alphabet_war('smzwszfbsgsqbzdwfcesqmwsqqep'))

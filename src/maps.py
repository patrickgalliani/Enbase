# Ricky Galliani


from collections import defaultdict

import random
import string


# Encoding maps
# Char -> Decimal Number
# Base Number Digit -> Char

def char_to_decimal_map(key):
    '''
    Maps alpha numeric characters in messages to decimal numbers.
    '''
    chars = list(string.printable)
    random.Random(key).shuffle(chars)
    return dict([(' ', 0)] + [(c, i + 1) for (i, c) in enumerate(chars)])


def digit_to_char_map(key):
    '''
    Maps base number digits to characters. Used in encoding messages.
    '''
    mp = defaultdict(list)
    chars = [c for c in string.printable if c.isalnum()]
    random.Random(key).shuffle(chars)
    for i, c in enumerate(chars):
        mp[i % 11].append(c)
    return mp


# Decoding maps
# Char -> Base Number Digit
# Decimal Number -> Char


def char_to_digit_map(key):
    '''
    Maps alpha numeric characters in encoded messages to digits. Used in decoding
    messages.
    '''
    return dict([(x, k) for (k, v) in digit_to_char_map(key).items() for x in v])


def decimal_to_char_map(key):
    '''
    Maps decimal numbers to alpha numeric characters. Used in decoding
    messages.
    '''
    return dict([(v, k) for (k, v) in char_to_decimal_map(key).items()])


# Ricky Galliani


from base_number import BaseNumber, decimal_to_base
from maps import (
    decimal_to_char_map,
    char_to_decimal_map,
    char_to_digit_map,
    digit_to_char_map
)

from random import choice


class EncodedMessage:

    def __init__(self, text, key):
        self.text = text
        self.key = key

    def __str__(self):
        return "EncodedMessage(text={}, key={})".format(self.text, self.key)

    def decode(self):
        '''
        Returns a Message.
        '''
        # Pull in encoding maps
        decimal_to_char = decimal_to_char_map()
        char_to_digit = char_to_digit_map(self.key)

        # Pull the chars used as spaces for this key
        space_holdout_chars = [k for (k, v) in char_to_digit.items() if v == 10]
        encoded_text = []
        cur_token = ''
        for c in self.text:
            if c not in space_holdout_chars:
                cur_token += c
            else:
                encoded_text.append(cur_token)
                cur_token = ''
        if cur_token != '':
            encoded_text.append(cur_token)
        
        decoded_text = ''
        for token in encoded_text:
            # Convert chars back to digits of a base number
            base_num_digits = ''
            for c in token:
                base_num_digits += str(char_to_digit[c])

            # Create base number with digits and key
            base_num = BaseNumber(base_num_digits, self.key)

            # Convert base number back to decimal
            num = base_num.as_decimal()

            # Convert decimal number back to a char
            decoded_text += decimal_to_char[num]
        return Message(decoded_text, self.key)


class Message:

    def __init__(self, text, key=None):
        self.text = text
        self.key = key

    def __str__(self):
        return "Message(text={}, key={})".format(self.text, self.key)

    def encode(self):
        '''
        Returns an EncodedMessage.
        '''
        key = choice(range(2, 10))  # Randomly assign key to this message
        encoded_text = ''
        char_to_decimal = char_to_decimal_map()
        digit_to_char = digit_to_char_map(key)
        def encode_char(c):
            # Convert each char to a decimal number
            num  = char_to_decimal[c]  
        
            # Convert each number into base given by key
            base_num = decimal_to_base(num, key)
            
            # Convert digits in base number back to chars
            encoded_char = ''
            for d in map(int, base_num.digits):
                encoded_char += choice(digit_to_char[d])
            return encoded_char

        # Chars held out to encode spaces are stored in position 10
        space_holdout_chars = digit_to_char[10]
        for c in self.text[:-1]:
            encoded_text += encode_char(c) + choice(space_holdout_chars)
        encoded_text += encode_char(self.text[-1])

        return EncodedMessage(encoded_text, key)




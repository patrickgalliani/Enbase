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

	Decoding algorithm:
	    1. Separate encoded messages into characters from original message
	    2. For each char in the encoded message
                - Convert char to digit of a base number
                - Convert base number back to decimal number
                - Convert decimal number to a char in the decoded message
        '''
        # Pull in the decoding maps
        decimal_to_char = decimal_to_char_map(self.key)
        char_to_digit = char_to_digit_map(self.key)

        space_holdout_chars = [k for (k, v) in char_to_digit.items() if v == 10]
        encoded_text = []
        cur_encoded_char = ''
        for l in self.text:
            if l not in space_holdout_chars:
                cur_encoded_char += l
            else:
                encoded_text.append(cur_encoded_char)
                cur_encoded_char = ''
        if cur_encoded_char != '':
            encoded_text.append(cur_encoded_char)
        
        decoded_text = ''
        for char in encoded_text:
            # Convert chars back to digits of a base number
            base_num_digits = ''
            for c in char:
                base_num_digits += str(char_to_digit[c])

            # Create base number with digits and key
            base_num = BaseNumber(base_num_digits, self.key)

            # Convert base number back to decimal
            num = base_num.as_decimal()

            # Convert decimal number back to a char
            decoded_text += decimal_to_char[num]
        return Message(decoded_text)


class Message:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Message(text={})".format(self.text)

    def encode(self):
        '''
        Returns an EncodedMessage.

	Encoding algorithm:
            1. Randomly choose key (determines base for decimal -> base number
               conversion)
            2. Put message text and key in string
            3. For each char in the string
                - Map char to a decimal number
                - Convert decimal number to a base system given by key
                - Convert base number digits back to chars
	    4. Append an encoded 'space' character to each encoded char
        '''
        # Randomly assign key to this message
        key = choice(range(2, 10))

        # Pull in the encoding maps
        char_to_decimal = char_to_decimal_map(key)
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
        encoded_text = ''
        for c in self.text:
            encoded_text += encode_char(c) + choice(space_holdout_chars)

        return EncodedMessage(encoded_text, key)


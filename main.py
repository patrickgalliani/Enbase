# Ricky Galliani

from src.base_number import decimal_to_base, BaseNumber
from src.message import EncodedMessage, Message


if __name__ == '__main__':

    m = Message('test message')
    print(m)
    encoded_m = m.encode()
    print("encoded m: {}".format(encoded_m))
    print("decoded m: {}".format(encoded_m.decode()))

    print
    print

    m2 = Message("What up, my name's Ricky Galliani. Does this still work?")
    print(m2)
    encoded_m2 = m2.encode()
    print("encoded m2: {}".format(encoded_m2))
    print("decoded m2: {}".format(encoded_m2.decode()))

    print
    print

    m3 = Message("Testing, testing, testing. Am I live?")
    print(m3)
    encoded_m3 = m3.encode()
    print("encoded m3: {}".format(encoded_m3))
    print("decoded m3: {}".format(encoded_m3.decode()))

  

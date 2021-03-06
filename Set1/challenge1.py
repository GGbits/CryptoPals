# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 1
# https://cryptopals.com/sets/1/challenges/1
#
# Description: The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import binascii
import base64


def hex_to_base64(hexed_string):
    """
    Base64 encodes a hexed string.
    :param hexed_string: hexed string to be base64 encoded.
    :return: base64 encoded string
    """
    # Remove hex encoding
    unhexed_string = binascii.unhexlify(hexed_string)
    # Encode base64 and return
    return base64.b64encode(unhexed_string)


def base64_to_hex(b64_string):
    """
    hex encodes a Base64 encoded string.
    :param b64_string: Base64 string to be hex encoded.
    :return: hex encoded string
    """
    # Remove hex encoding
    unencoded_string = base64.b64decode(b64_string)
    # Encode base64 and return
    return binascii.hexlify(unencoded_string)

if __name__ == '__main__':
    print(hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c"
                        "696b65206120706f69736f6e6f7573206d757368726f6f6d"))

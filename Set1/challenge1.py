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
    unhexed_string = binascii.unhexlify(hexed_string)
    return base64.b64encode(unhexed_string)

print(hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))

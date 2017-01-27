# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 2
# https://cryptopals.com/sets/1/challenges/2
#
# Description:
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# should produce:
# 746865206b696420646f6e277420706c6179

import binascii


def xor_hex_strings(hex_string1, hex_string2):
    xor_list = []
    unhexed_string1 = binascii.unhexlify(hex_string1)
    unhexed_string2 = binascii.unhexlify(hex_string2)
    for n1, n2 in zip(unhexed_string1, unhexed_string2):
        xor_list.append(format((n1 ^ n2), 'x'))
    return ''.join(xor_list)

print(xor_hex_strings("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))

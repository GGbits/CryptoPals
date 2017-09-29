# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 3
# https://cryptopals.com/sets/1/challenges/3
#
# Description:
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
# How? Devise some method for "scoring" a piece of English plaintext.
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.

import binascii
import operator
import string

KEY = ""


def award_points(i):
    """
    Dictionary Switch containing point values for ascii character frequency

    Args:
        i: int representation of ascii chr

    Returns:
        score (int) of the character
    """
    switch_dict = {
        32: 10,
        101: 9,
        116: 6,
        97: 5,
        111: 5,
        105: 4,
        110: 4,
        115: 4,
        104: 4,
        114: 3,
        100: 2,
        108: 2
    }
    return switch_dict.get(i, 0)


def get_xor_score(encoded_string, key):
    """
    Gets the total "score" for a xor chr

    Args:
        encoded_string: (str) hex encoded string that has been xored with single key xor
        key: (int) integer representation of xor key

    Returns:
        the points (int) score of the key used
    """
    if all(c in string.hexdigits for c in encoded_string):
        unhexed_string = binascii.unhexlify(encoded_string)
    else:
        unhexed_string = encoded_string
    char_list = [char ^ key for char in unhexed_string]
    points = 0
    for int_val in char_list:
        points += award_points(int_val)
    return points


def get_score(encoded_string):
    """
    Gets the total "score" for a hexed string

    Args:
        encoded_string: (str) hex encoded string that has been xored with single key xor

    Returns:
        the points (int) score of the key used
    """
    unhexed_string = binascii.unhexlify(encoded_string)
    char_list = [char for char in unhexed_string]
    points = 0
    for int_val in char_list:
        points += award_points(int_val)
    return points


def find_single_xor(encoded_string):
    xor_dict = {}
    for i in range(32, 127):
        score = get_xor_score(encoded_string, i)
        xor_dict.update({i: score})
    key = max(iter(xor_dict.items()), key=operator.itemgetter(1))
    return key


def decrypt_sk_xor_message(encoded_string, key):
    unhexed_string = binascii.unhexlify(encoded_string)
    char_list = [chr(char ^ key) for char in unhexed_string]
    return ''.join(char_list)


if __name__ == '__main__':

    KEY = find_single_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    MESSAGE = decrypt_sk_xor_message("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", KEY[0])
    print("Key: " + chr(KEY[0]) + "\nMessage: " + MESSAGE)

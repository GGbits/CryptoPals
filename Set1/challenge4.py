# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 4
# https://cryptopals.com/sets/1/challenges/4
#
# Description:
# One of the 60-character strings in 4.txt has been encrypted by single-character XOR.
# Find it.

import operator
from challenge3 import decrypt_sk_xor_message, find_single_xor


def import_string_from_file(file_path):
    with open(file_path, 'r') as file:
        text_list = [line.strip() for line in file]
    file.close()
    return text_list


def get_score_for_list(hex_list):
    score_list = [find_single_xor(hexed) for hexed in hex_list]
    return score_list


def find_xored_string(score_list):
    xored_index = max(score_list, key=operator.itemgetter(1))
    return xored_index[0], score_list.index(xored_index)


if __name__ == '__main__':
    hexed_text = import_string_from_file("..\\resources\\4.txt")
    scores_list = get_score_for_list(hexed_text)
    xored_key_index = find_xored_string(scores_list)
    message = decrypt_sk_xor_message(hexed_text[xored_key_index[1]], xored_key_index[0])
    print("Key: '" + chr(xored_key_index[0]) + "'\n" + "Message: " + message)


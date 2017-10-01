# Python Version: 3.5
# Creator - GGbits
# Set: 2
# Challenge: 11
# https://cryptopals.com/sets/2/challenges/11
#
# Description:

# Now that you have ECB and CBC working:
# Write a function to generate a random AES key; that's just 16 random bytes.
#
# Write a function that encrypts data under an unknown key --- that is,
# a function that generates a random key and encrypts under it.
# The function should look like:
# encryption_oracle(your-input)
# => [MEANINGLESS JIBBER JABBER]
# Under the hood, have the function append 5-10 bytes (count chosen randomly)
# before the plaintext and 5-10 bytes after the plaintext.
#
# Now, have the function choose to encrypt under ECB 1/2 the time,
# and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.
# Detect the block cipher mode the function is using each time.
# You should end up with a piece of code that, pointed at a block box that might be encrypting ECB or CBC,
# tells you which one is happening.

from challenge8 import chunks
from challenge10 import encrypt_cbc, encrypt_ecb
import os
from random import randint

test_message = b"ABC" * 80


def random_aes_key(size):
    return os.urandom(size)


def randomize_message(message):
    return b"".join([random_aes_key(randint(5, 10)), message, random_aes_key(randint(5, 10))])


def encrypt_ecb_or_cbc(message, key, blocksize):
    rand_msg = randomize_message(message)
    random_enc = (randint(0, 1))
    if random_enc == 0:
        iv = random_aes_key(16)
        return encrypt_cbc(rand_msg, key, iv, blocksize)
    else:
        return encrypt_ecb(rand_msg, key)


def detect_cbc_or_ebc(encrypted_string):
    blocks = chunks(encrypted_string, 16)
    num_blocks = len(blocks)
    # count number of distinct blocks
    distinct_blocks = {}
    for b in blocks:
        distinct_blocks[b] = 1
    num_distinct_blocks = len(distinct_blocks)
    if num_distinct_blocks < num_blocks:
        return "ECB"
    else:
        return "CBC"


if __name__ == '__main__':
    encrypt_string = encrypt_ecb_or_cbc(test_message, random_aes_key(16), 16)
    print(encrypt_string)
    print(detect_cbc_or_ebc(encrypt_string))

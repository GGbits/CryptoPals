# Python Version: 3.5
# Creator - GGbits
# Set: 2
# Challenge: 12
# https://cryptopals.com/sets/2/challenges/11
#
# Description:

# Byte-at-a-time ECB decryption (Simple)
# Copy your oracle function to a new function that encrypts buffers under ECB mode using a consistent but unknown key (for instance, assign a single random key, once, to a global variable).
#
# Now take that same function and have it append to the plaintext, BEFORE ENCRYPTING, the following string:
#
# Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
# aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
# dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
# YnkK
#
# Spoiler alert.
# Do not decode this string now. Don't do it.
#
# Base64 decode the string before appending it. Do not base64 decode the string by hand; make your code do it. The point is that you don't know its contents.
#
# What you have now is a function that produces:
#
# AES-128-ECB(your-string || unknown-string, random-key)
# It turns out: you can decrypt "unknown-string" with repeated calls to the oracle function!
#
# Here's roughly how:
#
# 1. Feed identical bytes of your-string to the function 1 at a time ---
# start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the block size of the cipher.
# You know it, but do this step anyway.
#
# 2. Detect that the function is using ECB. You already know, but do this step anyways.
#
# 3. Knowing the block size, craft an input block that is exactly 1 byte short
# (for instance, if the block size is 8 bytes, make "AAAAAAA").
# Think about what the oracle function is going to put in that last byte position.
#
# 4. Make a dictionary of every possible last byte by feeding different strings to the oracle; for instance,
# "AAAAAAAA", "AAAAAAAB", "AAAAAAAC", remembering the first block of each invocation.
#
# 5. Match the output of the one-byte-short input to one of the entries in your dictionary.
# You've now discovered the first byte of unknown-string.
# 6. Repeat for the next byte.

from challenge10 import encrypt_ecb
from challenge11 import detect_cbc_or_ebc, random_aes_key
import base64

# Variables
ecb_key = random_aes_key(16)
buffer_text = b"A" * 47
base64_provided_string = ("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
                          "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
                          "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
                          "YnkK")


def append_b64_string(bin_string, b64_string):
    return bin_string + base64.b64decode(b64_string)


def encrypt_buffer(message, key):
    return encrypt_ecb(message, key)


def find_key_length(encrypted, key, buffer_chr):
    key_length = 1
    while True:
        temp_message = buffer_chr * key_length
        temp_encrypt = encrypt_ecb(temp_message, key)
        if temp_encrypt[0:key_length] == encrypted[0:key_length]:
            return key_length
        if key_length == 128:
            return False
        key_length += 1


def get_unicode_character(int_code):
    return chr(int_code).encode()


def find_last_byte(enc_block, key, known_string):
    for i in range(0, 128):
        guess = known_string + get_unicode_character(i)
        if enc_block == (encrypt_ecb(guess, key)):
            return bytes([guess[-1]])


def decrypt_ecb_string(appended_string, buffer_length, key):
    block_length = len(key)
    decrypt_array = []
    buff_array = []
    for c in appended_string[buffer_length - block_length:buffer_length - 1]:
        buff_array.append(bytes([c]))
    for i in range(0, len(appended_message) - buffer_length):
        known = b"".join(buff_array[i: i + block_length - 1])
        encrypt_block = encrypt_ecb(appended_string[i + buffer_length - block_length + 1: i + buffer_length + 1], key)
        decrypt_char = find_last_byte(encrypt_block, key, known)
        decrypt_array.append(decrypt_char)
        buff_array.append(decrypt_char)
    return b"".join(decrypt_array)

if __name__ == '__main__':
    appended_message = append_b64_string(buffer_text, base64_provided_string)
    encrypted_string = encrypt_ecb(appended_message, ecb_key)
    print("1. Detect Key Size:")
    key_length = find_key_length(encrypted_string, ecb_key, b"A")
    print(key_length)
    print("2. Detect CBC or ECB: ")
    print(detect_cbc_or_ebc(encrypted_string))
    print("3-5. Find the first byte")
    test_string = encrypt_ecb(append_b64_string(b"A" * 15, base64_provided_string), ecb_key)
    print(find_last_byte(test_string[0:16], ecb_key, b"A" * 15))
    print("6. Solve encrypted string")
    print(decrypt_ecb_string(appended_message, 47, ecb_key))


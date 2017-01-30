# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 6
# https://cryptopals.com/sets/1/challenges/6
#
# Description:
# Here is the opening stanza of an important work of the English language:
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
# Encrypt it, under the key "ICE", using repeating-key XOR.
# In repeating-key XOR, you'll sequentially apply each byte of the key;
# the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.
# It should come out to:
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427276527
# 2a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

# The file 6.txt has been base64'd after being encrypted with repeating-key XOR.
#
# Decrypt it.
#
# Here's how:
#
# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# Write a function to compute the edit distance/Hamming distance between two strings.
# The Hamming distance is just the number of differing bits. The distance between:
# "this is a test" and "wokka wokka!!!" is 37. Make sure your code agrees before you proceed.

# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
# and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
# The KEYSIZE with the smallest normalized edit distance is probably the key.
# You could proceed perhaps with the smallest 2-3 KEYSIZE values.
# Or take 4 KEYSIZE blocks instead of 2 and average the distances.
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
# Now transpose the blocks: make a block that is the first byte of every block,
# and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to do this.
# For each block, the single-byte XOR key that produces the best looking histogram
# is the repeating-key XOR key byte for that block. Put them together and you have the key.
# This code is going to turn out to be surprisingly useful later on.
# Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing.
# But more people "know how" to break it than can actually break it,
# and a similar technique breaks something much more important.
import base64
import binascii
from challenge4 import import_string_from_file


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def decrypt_base64(base64_string):
    return base64.b64decode(base64_string)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def hamming_distance(string1, string2):
    assert len(string1) == len(string2)
    if type(string1) is str and type(string2 is str):
        string1 = text_to_bits(string1)
        string2 = text_to_bits(string2)
    # TODO: if byte array, turn into binary string
    counter = 0
    for b1, b2 in zip(string1, string2):
        if b1 != b2:
            counter += 1
    return counter


def find_key_length(bin_string):
    keysize = 2
    hamming_results = []
    while keysize < 41:
        counter = 0
        hamming_temp = []
        while counter + keysize * 2 < len(bin_string):
            hd_string1 = bin_string[counter: counter + keysize]
            hd_string2 = bin_string[counter + keysize: counter + keysize * 2]
            hamming_temp.append(hamming_distance(hd_string1, hd_string2))
            counter += keysize * 2
        hamming_results.append({"keysize": keysize, "hamming": sum(hamming_temp) / float(len(hamming_temp))})
        keysize += 1
    return min(iter(hamming_results), key=lambda x: x['hamming'])

if __name__ == '__main__':
    b64_string = ''.join(import_string_from_file("..\\resources\\6.txt"))
    decoded_byte_string = decrypt_base64(b64_string)
    print(decoded_byte_string)
    print(type(decoded_byte_string))
    print(hamming_distance("this is a test", "wokka wokka!!!"))
    print(find_key_length(decoded_byte_string))

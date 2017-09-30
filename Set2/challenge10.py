# Python Version: 3.5
# Creator - GGbits
# Set: 2
# Challenge: 10
# https://cryptopals.com/sets/2/challenges/10
#
# Description:
# CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages,
# despite the fact that a block cipher natively only transforms individual blocks.

# In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.
# The first plaintext block, which has no associated previous ciphertext block,
# is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

# Implement CBC mode by hand by taking the ECB function you wrote earlier,
# making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test),
# and using your XOR function from the previous exercise to combine them.

# The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0
# (\x00\x00\x00 &c)

from challenge4 import import_string_from_file
from challenge7 import decrypt_aes_128_ecb, encrypt_aes_128_ecb
from challenge8 import chunks
from challenge9 import pad_text

# Variables

init_vect = b"\x00" * 16


def encrypt_cbc(message, key, iv, blocksize):
    encrypt_array = []
    block_array = chunks(message, blocksize)
    if len(block_array[-1]) != blocksize:
        block_array[-1] = pad_text(block_array[-1], 16)
    for i in range(0, len(block_array)):
        xor_block = bytes((b1 ^ b2) for b1, b2 in zip(block_array[i], iv))
        iv = encrypt_aes_128_ecb(xor_block, key)
        encrypt_array.append(iv)
    return b"".join(encrypt_array)


if __name__ == '__main__':
    # TODO: This ECB Decrypts, need to work with it to make it CBC
    string_to_encrypt = "\r\n".join(import_string_from_file("..\\resources\\10_mytest.txt")).encode()
    encrypted_string = encrypt_cbc(string_to_encrypt, b"YELLOW SUBMARINE", init_vect, 16)
    print(encrypted_string)
    print(encrypted_string.decode("utf-8"))

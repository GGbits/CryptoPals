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

from challenge7 import decrypt_aes_128_ecb, encrypt_aes_128_ecb
from challenge9 import pad_text


if __name__ == '__main__':
    # TODO: This ECB Decrypts, need to work with it to make it CBC
    padded = pad_text("WHATS IN A NAME?", 16)
    print(padded)
    encrypted = encrypt_aes_128_ecb(padded, b'YELLOW SUBMARINE')
    decrypted = decrypt_aes_128_ecb(encrypted, b'YELLOW SUBMARINE')
    print(encrypted)
    print(decrypted)

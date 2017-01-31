# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 7
# https://cryptopals.com/sets/1/challenges/7
#
# Description:
# The Base64-encoded content in the 7.txt file has been encrypted via AES-128 in ECB mode under the key
#"YELLOW SUBMARINE".
#(case-sensitive, without the quotes; exactly 16 characters;
# I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).
#Decrypt it. You know the key, after all.
#Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
from Crypto.Cipher import AES
from challenge4 import import_string_from_file
import base64


def decrypt_aes_128_ecb(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(text)

if __name__ == '__main__':
    aes_string = base64.b64decode(''.join(import_string_from_file("..\\resources\\7.txt")))
    decrypted_string = decrypt_aes_128_ecb(aes_string, b'YELLOW SUBMARINE')
    print(decrypted_string)

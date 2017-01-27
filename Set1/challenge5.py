# Python Version: 3.5
# Creator - GGbits
# Set: 1
# Challenge: 5
# https://cryptopals.com/sets/1/challenges/5
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


def xor_repeting_key(string, key):
    """
    Converts text string to XORed encrypted hex using the supplied ASCII key.
    :param string: ascii string to be XORed and HEXed
    :param key: ASCII Key (string) used to xor against string
    :return: XORed hex string
    """
    key_index = 0
    xor_list = []
    # For each chr in string...
    for char in string:
        # convert the key chr and string chr to digits, XOR them, then take the XORed value and hex it into a list
        xor_list.append(format(ord(char) ^ ord(key[key_index]), 'x').zfill(2))
        # If we are at the last letter of the key, start over from the first letter, else, move onto the next letter
        if key_index >= len(key) - 1:
            key_index = 0
        else:
            key_index += 1
    return ''.join(xor_list)

if __name__ == '__main__':
    print(xor_repeting_key("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", "ICE"))

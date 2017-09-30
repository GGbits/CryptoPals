# # Python Version: 3.5
# Creator - GGbits
# Set: 2
# Challenge: 9
# https://cryptopals.com/sets/2/challenges/9
#
# Description:
# A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext.
# But we almost never want to transform a single block; we encrypt irregularly-sized messages.
# One way we account for irregularly-sized messages is by padding,
# creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.
# So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block.
# For instance:
# "YELLOW SUBMARINE"
# ... padded to 20 bytes would be:
# "YELLOW SUBMARINE\x04\x04\x04\x04"


def pad_text(text, byte_length):
    if type(text) is str:
        binary_text = text.encode('UTF-8')
    else:
        binary_text = text
    trail = byte_length - len(binary_text) % byte_length
    if trail != byte_length:
        count = 0
        while count < trail:
            binary_text += b'\x04'
            count += 1
    return binary_text.decode('UTF-8')

if __name__ == '__main__':
    bin_data = pad_text("YELLOW SUBMARINE", 20)
    print(bin_data)

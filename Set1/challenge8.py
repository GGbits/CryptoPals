from challenge4 import import_string_from_file


def chunks(array, n):
    return [array[i:i+n] for i in range(0, len(array), n)]


def detect_ecb(ciphers):
    result = []
    for cip in ciphers:
        # split into 16-byte blocks
        splits = chunks(cip, 16)
        num_blocks = len(splits)
        # count number of distinct blocks
        distinct_blocks = {}
        for s in splits:
            distinct_blocks[s] = 1
        num_distinct_blocks = len(distinct_blocks)
        if num_distinct_blocks < num_blocks:
            result.append(cip)
    return result


if __name__ == '__main__':
    hex_list = import_string_from_file("..\\resources\\8.txt")
    print(detect_ecb(hex_list))

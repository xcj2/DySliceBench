# the uppercase letters are encoded as 65 to 90
# I want to put A as 0, so Z is 25

def letter_to_int(letter):
    return ord(letter)-65


def int_to_letter(encoded_value):
    return chr(encoded_value+65)


def shift_string(N, string):
    shifted_string = ""
    for char in string:
        encoding = letter_to_int(char)
        # mod ensures it wraps around, eg N=3 sends Z to C
        shifted = (encoding+N)%26
        decoded_to_letter = int_to_letter(shifted)
        shifted_string = shifted_string + decoded_to_letter
    return shifted_string


if __name__ == "__main__":
    test1 = \
"""2
ABCXYZ"""
    test2 = \
"""0
ABCXYZ"""
    test3 = \
"""13
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    various_tests = [test1, test2, test3]
    """for test in various_tests:
        lines = test.split("\n")
        N = int(lines[0])
        string = lines[1]
        print(shift_string(N, string))"""
    N = int(input())
    string = input()
    print(shift_string(N, string))
import re
import functools

class IO_for_Contest(object):
    @staticmethod
    def my_input():
        #return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        #TODO: impl this for each problem
        pass

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(int, re.split(' ', IO_for_Contest.my_input().strip())))[ : n]


def solve():
    a, b = IO_for_Contest.read_n_int(2)
    result = get_result(a, b)
    print(result)

def get_result(a, b):
    if a * b == 0:
        return 'Zero'
    if a * b < 0:
        return 'Zero'
    if a > 0:
        return 'Positive'
    if abs(b - a) % 2 == 0:
        return 'Negative'
    return 'Positive'

if __name__ == '__main__':
    solve()

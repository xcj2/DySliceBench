import re
# import doctest


class IO_for_Contest(object):
    @staticmethod
    def my_input():
        # return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        pass

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(
                    int,
                    re.split('\s+', IO_for_Contest.my_input().strip())))[: n]


def solve():
    buf = IO_for_Contest.read_n_int(3)
    a = buf[0]
    b = buf[1]
    c = buf[2]
    print(min_diff(a, b, c,))


def min_diff(a, b, c):
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        return 0
    diff = a * b * c
    diff = min(diff, abs(a * b * (c // 2) - a * b * (c - (c // 2))))
    diff = min(diff, abs(a * (b // 2) * c - a * (b - (b // 2)) * c))
    diff = min(diff, abs((a // 2) * b * c - (a - (a // 2)) * b * c))
    return diff

if __name__ == '__main__':
    # doctest.testmod()
    solve()
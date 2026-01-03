import re
import doctest


class IO_for_Contest(object):
    @staticmethod
    def my_input():
        # return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        return IO_for_Contest.read_n_int(3)

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
    a = IO_for_Contest.read_from_input()
    a.sort()
    if is_legal(a):
        print('YES')
    else:
        print('NO')


def is_legal(a):
    return len(a) == 3 and a[0] == 5 and a[1] == 5 and a[2] == 7

if __name__ == '__main__':
    # doctest.testmod()
    solve()
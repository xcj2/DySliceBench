import unittest
import math


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2), 3)

    def test_2(self):
        self.assertEqual(think(4), 7)

    def test_3(self):
        self.assertEqual(think(1000000000000), 1099511627775)


def solve():
    h = read()
    result = think(h)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return read_type(int, n, sep=' ')


def read_float(n):
    return read_type(float, n, sep=' ')


def read_type(t, n, sep):
    return list(map(lambda x: t(x), read_line().split(sep)))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(h):
    rank = math.floor(math.log(h) / math.log(2)) + 1
    return 2 ** rank - 1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
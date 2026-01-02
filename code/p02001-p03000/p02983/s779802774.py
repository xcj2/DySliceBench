import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2020, 2040), 2)

    def test_2(self):
        self.assertEqual(think(4, 5), 20)


def solve():
    l, r = read()
    result = think(l, r)
    write(result)


def read():
    return read_int(2)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(l, r):
    mode = 2019
    m = 2018

    for i in range(l, r):
        for j in range(i + 1, r + 1):
            if i % mode == 0 or j % mode == 0:
                return 0
            m = min(m, (i % mode * j % mode) % mode)
    return m


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(150, [150, 140, 100, 200]), 2)

    def test_2(self):
        self.assertEqual(think(500, [499]), 0)

    def test_3(self):
        self.assertEqual(think(1, [100, 200, 300, 400, 500]), 5)


def solve():
    k, h = read()
    result = think(k, h)
    write(result)


def read():
    n, k = read_int(2)
    h = read_int(n)
    return k, h


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(k, h):
    return len(list(filter(lambda x: x >= k, h)))


def write(result):
    print(result)


if __name__ == '__main__':
    # import sys
    # sys.setrecursionlimit(10000)
    # unittest.main()
    solve()
import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, 2, 9), 8)

    def test_2(self):
        self.assertEqual(think(4, 2, 7), 7)

    def test_3(self):
        self.assertEqual(think(4, 2, 8), 8)


def solve():
    n, a, b = read_int(3)
    result = think(n, a, b)
    write(result)


def read():
    return read_int(3)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, a, b):
    return min(b, a * n)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
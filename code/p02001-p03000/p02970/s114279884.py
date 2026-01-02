import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(6, 2), 2)

    def test_2(self):
        self.assertEqual(think(14, 3), 2)

    def test_3(self):
        self.assertEqual(think(20, 4), 3)


def solve():
    n, d = read()
    result = think(n, d)
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


def think(n, d):
    territory = 2 * d + 1
    if n % territory == 0:
        return n // territory
    return n // territory + 1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
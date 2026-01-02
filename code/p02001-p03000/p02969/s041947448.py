import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4), 48)

    def test_2(self):
        self.assertEqual(think(15), 675)

    def test_3(self):
        self.assertEqual(think(80), 19200)


def solve():
    r = read()
    result = think(r)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(r):
    return 3 * r ** 2


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
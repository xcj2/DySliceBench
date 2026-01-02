import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(3, 5), 0)

    def test_2(self):
        self.assertEqual(think(7, 5), 10)

    def test_3(self):
        self.assertEqual(think(6, 6), 10)


def solve():
    x, a = read()
    result = think(x, a)
    write(result)


def read():
    return read_int(2)


def read_int(n):
    return read_type(int, n)


def read_float(n):
    return read_type(float, n)


def read_type(t, n):
    return list(map(lambda x: t(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(x, a):
    return 0 if x < a else 10


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
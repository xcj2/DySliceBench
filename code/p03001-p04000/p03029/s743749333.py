import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(1, 3), 3)

    def test_2(self):
        self.assertEqual(think(0, 1), 0)

    def test_3(self):
        self.assertEqual(think(32, 21), 58)


def solve():
    a, p = read()
    result = think(a, p)
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


def think(a, p):
    return (a * 3 + p) // 2


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
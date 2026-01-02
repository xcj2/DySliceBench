import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 900), 'Yes')

    def test_2(self):
        self.assertEqual(think(1, 501), 'No')

    def test_3(self):
        self.assertEqual(think(4, 2000), 'Yes')


def solve():
    k, x = read()
    result = think(k, x)
    write(result)


def read():
    return read_int(2)


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


def think(k, x):
    unit = 500
    return 'Yes' if unit * k >= x else 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
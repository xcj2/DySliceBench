import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(30, 100), 100)

    def test_2(self):
        self.assertEqual(think(12, 100), 50)

    def test_3(self):
        self.assertEqual(think(0, 100), 0)


def solve():
    a, b = read()
    result = think(a, b)
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


def think(a, b):
    if a <= 5:
        return 0
    elif a <= 12:
        return b // 2
    return b


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
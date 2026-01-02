import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([2, 6, 1, 4, 5]), 'YES')

    def test_2(self):
        self.assertEqual(think([4, 1, 3, 1, 6, 2]), 'NO')

    def test_3(self):
        self.assertEqual(think([10000000, 10000000]), 'NO')


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


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


def think(a):
    return 'YES' if len(a) == len(set(a)) else 'NO'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()

import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(8, 3, 4), 4)

    def test_2(self):
        self.assertEqual(think(8, 0, 4), 0)

    def test_3(self):
        self.assertEqual(think(6, 2, 4), 2)


def solve():
    n, a, b = read()
    result = think(n, a, b)
    write(result)


def read():
    return read_int(3)


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


def think(n, a, b):
    mode = a + b
    if n % mode == 0:
        return a * (n // mode)
    else:
        blue = a * (n // mode)
        remain = n - (n // mode) * mode
        if a <= remain:
            return blue + a
        else:
            return blue + remain


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
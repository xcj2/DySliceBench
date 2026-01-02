import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(11, 2), 4)

    def test_2(self):
        self.assertEqual(think(1010101, 10), 7)

    def test_3(self):
        self.assertEqual(think(314159265, 3), 18)


def solve():
    n, k = read()
    result = think(n, k)
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


def think(n, k):
    buf = ''
    while n > 0:
        buf += str(n % k)
        n //= k
    return len(buf)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
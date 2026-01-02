import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, 5), 10)

    def test_2(self):
        self.assertEqual(think(7, 3), 11)


def solve():
    h, w = read()
    result = think(h, w)
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


def think(h, w):
    if h == 1 or w == 1:
        return 1
    if w % 2 == 0:
        return w // 2 * h
    else:
        if h % 2 == 0:
            return w * (h // 2)
        else:
            return w * (h // 2) + (w // 2) + 1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
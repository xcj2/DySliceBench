import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('sardine'), 'xxxxxxx')

    def test_2(self):
        self.assertEqual(think('xxxx'), 'xxxx')

    def test_3(self):
        self.assertEqual(think('gone'), 'xxxx')


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    return read_line()


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


def think(s):
    return 'x' * len(s)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()

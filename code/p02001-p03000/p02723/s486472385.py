import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('sippuu'), 'Yes')

    def test_2(self):
        self.assertEqual(think('iphone'), 'No')

    def test_3(self):
        self.assertEqual(think('coffee'), 'Yes')


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


def think(data):
    return 'Yes' if data[2] == data[3] and data[4] == data[5] else 'No'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
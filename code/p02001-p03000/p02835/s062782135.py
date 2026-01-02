import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([5, 7, 9]), 'win')

    def test_2(self):
        self.assertEqual(think([13, 7, 2]), 'bust')


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    return read_int(3)


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


def think(data):
    a1, a2, a3 = data
    if a1 + a2 + a3 < 22:
        return 'win'
    return 'bust'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
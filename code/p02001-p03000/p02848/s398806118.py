import unittest
import string


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, 'ABCXYZ'), 'CDEZAB')

    def test_2(self):
        self.assertEqual(think(0, 'ABCXYZ'), 'ABCXYZ')

    def test_3(self):
        self.assertEqual(think(13, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'NOPQRSTUVWXYZABCDEFGHIJKLM')


def solve():
    n, s = read()
    result = think(n, s)
    write(result)


def read():
    n = read_int(1)[0]
    s = read_line()
    return n, s


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


def think(n, s):
    result = ''
    d = string.ascii_uppercase
    for c in s:
        index = d.index(c)
        new_index = (index + n) % len(d)
        result += d[new_index]
    return result


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
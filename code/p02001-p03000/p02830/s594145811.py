import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('ip', 'cc'), 'icpc')

    def test_2(self):
        self.assertEqual(think('hmhmnknk', 'uuuuuuuu'), 'humuhumunukunuku')

    def test_3(self):
        self.assertEqual(think('aaaaa', 'aaaaa'), 'aaaaaaaaaa')


def solve():
    s, t = read()
    result = think(s, t)
    write(result)


def read():
    n = read_int(1)[0]
    buf = read_line(n=2 * n + 1)
    return buf.split(" ")


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


def think(s, t):
    buf = ''
    for ss, tt in zip(s, t):
        buf += ss
        buf += tt
    return buf


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()

import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(1, 2), 3)


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    a = read_int(1)[0]
    b = read_int(1)[0]
    return a, b


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
    s = set()
    s.add(a)
    s.add(b)
    if 1 in s:
        if 2 in s:
            return 3
        else:
            return 2
    else:
        return 1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()

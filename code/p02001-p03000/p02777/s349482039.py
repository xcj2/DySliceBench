import unittest


class TestA(unittest.TestCase):
    def test_1(self):
        # (actual_value, expected_value)
        self.assertEqual(True, False)


def solve():
    s, t, a, b, u = read()
    result = think(s, t, a, b, u)
    write(result)


def read():
    s, t = read_line().split(" ")
    a, b = read_int(2)
    u = read_line()
    return s, t, a, b, u


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


def think(s, t, a, b, u):
    if s == u:
        return a - 1, b
    else:
        return a, b - 1


def write(result):
    print(result[0], result[1])


if __name__ == '__main__':
    # unittest.main()
    solve()

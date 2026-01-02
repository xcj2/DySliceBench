import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(1024), 2020)

    def test_2(self):
        self.assertEqual(think(0), 0)

    def test_3(self):
        self.assertEqual(think(1000000000), 2000000000)


def solve():
    x = read()
    result = think(x)
    write(result)


def read():
    return read_int(1)[0]


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
    result = 1000 * (data // 500)
    data %= 500
    result += 5 * (data // 5)
    return result


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
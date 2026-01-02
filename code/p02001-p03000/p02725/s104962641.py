import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(20, [5, 10, 15]), 10)

    def test_2(self):
        self.assertEqual(think(20, [0, 5, 15]), 10)


def solve():
    k, a = read()
    result = think(k, a)
    write(result)


def read():
    k, n = read_int(2)
    return k, read_int(n)


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


def think(k, a):
    distance = []
    for i in range(len(a) - 1):
        distance.append(a[i + 1] - a[i])
    distance.append(k - a[-1] + a[0])
    return sum(distance) - max(distance)


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
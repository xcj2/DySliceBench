import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(6, [3, 4, 5]), 2)

    def test_2(self):
        self.assertEqual(think(9, [3, 3, 3, 3]), 4)


def solve():
    x, l = read()
    result = think(x, l)
    write(result)


def read():
    n, x = read_int(2)
    return x, read_int(n)


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


def think(x, l):
    count = 1
    s = 0
    for e in l:
        s += e
        if s > x:
            break
        count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
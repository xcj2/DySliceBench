import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([2, 1, 2]), 1)

    def test_2(self):
        self.assertEqual(think([2, 2, 2]), -1)

    def test_3(self):
        self.assertEqual(think([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), 7)


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


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


def think(a):
    if 1 not in a:
        return -1
    next_index = 1
    count = 0

    for i in a:
        if next_index == i:
            next_index += 1
        else:
            count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
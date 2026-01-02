import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([1, 2, 3]), 0)

    def test_2(self):
        self.assertEqual(think([1, 3, 1, 1]), 2)

    def test_3(self):
        self.assertEqual(think([27, 23, 76, 2, 3, 5, 62, 52]), 2)


def solve():
    w = read()
    result = think(w)
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


def think(w):
    s = sum(w)
    diff = 1e10
    accum = [0]
    for e in w:
        accum.append(accum[-1] + e)
    for i in range(len(accum)):
        diff = min(diff, abs(accum[i] - (s - accum[i])))
    return diff


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(2, [[1, 2], [2]], [0, 1]), 1)

    def test_2(self):
        self.assertEqual(think(2, [[1, 2], [1], [2]], [0, 0, 1]), 0)

    def test_3(self):
        self.assertEqual(think(5, [[1, 2, 5], [2, 3]], [1, 0]), 8)


def solve():
    n, s, p = read()
    result = think(n, s, p)
    write(result)


def read():
    n, m = read_int(2)
    s = []
    for _ in range(m):
        buf = read_line().split()
        k = int(buf[0])
        s.append(list(map(int, buf[1:k + 1])))
    p = read_int(m)
    return n, s, p


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


def think(n, s, p):
    count = 0
    m = len(s)
    for bit in range(2 ** n):
        satisfy = True
        for i in range(m):
            if satisfies_condition(bit, s[i], p[i]):
                continue
            satisfy = False
            break
        if satisfy:
            count += 1
    return count


def write(result):
    print(result)


def satisfies_condition(bit, s, p):
    result = 0
    for ss in s:
        result ^= mask(bit, ss)
    return result == p


def mask(bit, k):
    return (bit >> (k - 1)) & 1


if __name__ == '__main__':
    # unittest.main()
    solve()
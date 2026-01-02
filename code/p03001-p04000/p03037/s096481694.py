import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(4, [[1, 3], [2, 4]]),
            2
        )

    def test_2(self):
        self.assertEqual(
            think(10, [[3, 6], [5, 7], [6, 9]]),
            1
        )

    def test_3(self):
        self.assertEqual(
            think(100000, [[1, 100000]]),
            100000
        )


def solve():
    n, list_of_l_and_r = read()
    result = think(n, list_of_l_and_r)
    write(result)


def read():
    n, m = read_int(2)
    list_of_l_and_r = []
    for _ in range(m):
        list_of_l_and_r.append(read_int(2))
    return n, list_of_l_and_r


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


def think(n, list_of_l_and_r):
    left = 1
    right = n
    for l, r in list_of_l_and_r:
        if right < l or r < left:
            return 0
        left = max(l, left)
        right = min(r, right)
    return right - left + 1


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
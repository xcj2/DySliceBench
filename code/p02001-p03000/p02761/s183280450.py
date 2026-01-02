import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(3, [[1, 7], [3, 2], [1, 7]]), 702)

    def test_2(self):
        self.assertEqual(think(3, [[2, 1], [2, 3]]), -1)

    def test_3(self):
        self.assertEqual(think(3, [[1, 0]]), -1)

    def test_4(self):
        self.assertEqual(think(1, [[1, 0]]), 0)

    def test_5(self):
        self.assertEqual(think(1, []), 0)


def solve():
    n, list_of_s_and_c = read()
    result = think(n, list_of_s_and_c)
    write(result)


def read():
    n, m = read_int(2)
    list_of_s_and_c = []
    for _ in range(m):
        list_of_s_and_c.append(read_int(2))
    return n, list_of_s_and_c


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


def think(n, list_of_s_and_c):
    not_occupied = -1
    buf = [not_occupied] * n
    for s, c in list_of_s_and_c:
        index = s - 1
        if buf[index] == not_occupied:
            buf[index] = c
        else:
            if buf[index] == c:
                continue
            else:
                return -1
    for i in range(n):
        if buf[i] == not_occupied:
            if i == 0:
                if n == 1:
                    buf[i] = 0
                else:
                    buf[i] = 1
            else:
                buf[i] = 0

    if buf[0] == 0:
        if n == 1:
            return 0
        else:
            return -1
    return int(''.join(map(str, buf)))


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
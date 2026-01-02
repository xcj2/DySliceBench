import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([5, 2, 3, 4, 1]), 'YES')

    def test_2(self):
        self.assertEqual(think([2, 4, 3, 5, 1]), 'NO')

    def test_3(self):
        self.assertEqual(think([1, 2, 3, 4, 5, 6, 7]), 'YES')


def solve():
    p = read()
    result = think(p)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    reverse = []
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            if reverse:
                reverse.append(i)
            else:
                reverse.append(i - 1)
    if not reverse:
        return 'YES'

    if len(reverse) == 2:
        i, j = reverse
        data[i], data[j] = data[j], data[i]
        for i in range(1, len(data)):
            if data[i] < data[i - 1]:
                return 'NO'
        return 'YES'
    else:
        return 'NO'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
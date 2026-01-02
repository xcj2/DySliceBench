import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([3, 5, 2], [4, 5]), 9)

    def test_2(self):
        self.assertEqual(think([5, 6, 3, 8], [5, 100, 8]), 22)

    def test_3(self):
        self.assertEqual(think([100, 1, 1], [1, 100]), 3)


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    n = read_int(1)[0]
    a = read_int(n + 1)
    b = read_int(n)
    return a, b


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b):
    count = 0
    for index, value in enumerate(b):
        if a[index] + a[index + 1] <= value:
            count += a[index] + a[index + 1]
            a[index] = 0
            a[index + 1] = 0
        else:
            if a[index] <= value:
                count += a[index]
                value -= a[index]
                a[index] = 0
                if value > 0:
                    count += value
                    a[index + 1] -= value
            else:
                count += value
                a[index] -= value
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
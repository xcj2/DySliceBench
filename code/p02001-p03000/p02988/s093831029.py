import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([1, 3, 5, 4, 2]), 2)

    def test_2(self):
        self.assertEqual(think([9, 6, 3, 2, 5, 8, 7, 4, 1]), 5)


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
    n = len(data)
    count = 0
    for i in range(n):
        if i + 2 >= n:
            break
        if data[i] < data[i + 1] < data[i + 2] or data[i] > data[i + 1] > data[i + 2]:
            count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('redcoder'), 1)

    def test_2(self):
        self.assertEqual(think('vvvvv'), 0)

    def test_3(self):
        self.assertEqual(think('abcdabc'), 2)


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    return read_line()


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


def think(data):
    mid = len(data) // 2 - 1

    left = 0
    right = len(data) - 1
    count = 0
    while left <= mid:
        count += 0 if data[left] == data[right] else 1
        left += 1
        right -= 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
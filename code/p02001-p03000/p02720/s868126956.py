import unittest
import collections


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(15), 23)

    def test_2(self):
        self.assertEqual(think(1), 1)

    def test_3(self):
        self.assertEqual(think(13), 21)

    def test_4(self):
        self.assertEqual(think(100000), 3234566667)


def solve():
    k = read()
    result = think(k)
    write(result)


def read():
    return read_int(1)[0]


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


def think(k):
    k_max = 10 ** 5
    list_of_lunlun_number = prepare_lunlun_number(k_max)
    return list_of_lunlun_number[k - 1]


def write(result):
    print(result)


def prepare_lunlun_number(k_max):
    lunlun_number = collections.deque([])
    deque = collections.deque(list(range(1, 10)))
    length = 0
    while length < k_max:
        d = deque.popleft()
        lunlun_number.append(d)
        length += 1
        if d % 10 == 0:
            deque.append(d * 10 + 0)
            deque.append(d * 10 + 1)
        elif d % 10 == 9:
            deque.append(d * 10 + 8)
            deque.append(d * 10 + 9)
        else:
            m = d % 10
            deque.append(d * 10 + m - 1)
            deque.append(d * 10 + m)
            deque.append(d * 10 + m + 1)
    return lunlun_number


if __name__ == '__main__':
    # unittest.main()
    solve()
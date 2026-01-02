import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(4, [-10, 8, 2, 1, 2, 6]), 14)

    def test_2(self):
        self.assertEqual(think(4, [-6, -100, 50, -2, -5, -3]), 44)

    def test_3(self):
        self.assertEqual(think(3, [-6, -100, 50, -2, -5, -3]), 0)


def solve():
    k, v = read()
    result = think(k, v)
    write(result)


def read():
    n, k = read_int(2)
    return k, read_int(n)


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


def think(k, v):
    max_value = -(10 ** 10)

    max_dequeue = min(len(v), k)
    for dequeue in range(max_dequeue + 1):
        max_enqueue = min(k - dequeue, dequeue)
        for left in range(dequeue + 1):
            dequeued_v = []
            right = dequeue - left
            dequeued_v += v[0:left]
            dequeued_v += [] if right == 0 else v[-right:]
            dequeued_v.sort()
            for i in range(max_enqueue + 1):
                max_value = max(max_value, sum(dequeued_v[i:]))
    return max_value


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
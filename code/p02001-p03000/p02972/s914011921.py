import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        a = [1, 0, 0]
        b = think(a)
        self.assertEqual(is_valid(a, b), True)

    def test_2(self):
        a = [0, 0, 0, 0, 0]
        b = think(a)
        self.assertEqual(is_valid(a, b), True)

    def test_3(self):
        a = [1, 1, 1, 1, 1, 1, 1]
        b = think(a)
        self.assertEqual(is_valid(a, b), True)

    def test_4(self):
        a = [1, 1, 1, 0, 1, 1, 0, 0]
        b = think(a)
        self.assertEqual(is_valid(a, b), True)


def solve():
    a = read()
    b = think(a)
    write(b)


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


def think(a):
    b = [0 for x in range(len(a))]
    for i in range(len(a), 0, -1):
        # print(i)
        count = 0
        for j in range(i, len(a) + 1, i):
            # print(j, ' ', end='')
            count += b[j - 1]
        # print('', b, ',', count, ',', a[i - 1])
        if a[i - 1] % 2 == count % 2:
            b[i - 1] = 0
        else:
            b[i - 1] = 1
    result = []
    for i in range(len(b)):
        if b[i] == 1:
            result.append(i + 1)
    return result


def write(b):
    print(len(b))
    print(' '.join(list(map(str, b))))


def is_valid(a, b):
    buf = [0 for x in range(len(a))]
    for i in b:
        buf[i - 1] = 1
    for i in range(len(a)):
        mod = i + 1
        count = 0
        for j in range(len(a)):
            to_be_divided = j + 1
            if to_be_divided % mod == 0:
                if buf[j]:
                    count += 1
        if count % 2 == a[i]:
            continue
        return False
    return True


if __name__ == '__main__':
    # unittest.main()
    solve()
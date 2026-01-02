import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([6, 7, 9, 10, 31]), 'APPROVED')

    def test_2(self):
        self.assertEqual(think([28, 27, 24]), 'DENIED')


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


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


def think(a):
    approved = True
    for e in a:
        if e % 2 == 0:
            if e % 3 == 0 or e % 5 == 0:
                continue
            else:
                approved = False
                break
        else:
            continue
    return 'APPROVED' if approved else 'DENIED'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
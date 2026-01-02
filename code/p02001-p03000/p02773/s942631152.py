import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think(['beat', 'vet', 'beet', 'bed', 'vet', 'bet', 'beet']), ['beet', 'vet'])

    def test_2(self):
        self.assertEqual(think(['buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo']), ['buffalo'])

    def test_3(self):
        self.assertEqual(think(['bass', 'bass', 'kick', 'kick', 'bass', 'kick', 'kick']), ['kick'])

    def test_4(self):
        self.assertEqual(think(['ushi', 'tapu', 'nichia', 'kun']), ['kun', 'nichia', 'tapu', 'ushi'])


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    n = read_int(1)[0]
    s = []
    for _ in range(n):
        s.append(read_line())
    return s


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


def think(s):
    d = {}
    for e in s:
        d[e] = d.get(e, 0) + 1
    maximum = 0
    for key, value in d.items():
        maximum = max(maximum, value)
    result = []
    for key, value in d.items():
        if value == maximum:
            result.append(key)
    result.sort()
    return result


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    solve()
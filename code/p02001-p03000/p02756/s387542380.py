import unittest
import collections


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('a', ['2 1 p', '1', '2 2 c', '1']), 'cpa')

    def test_2(self):
        self.assertEqual(think('a', ['2 2 a', '2 1 b', '1', '2 2 c', '1', '1']), 'aabc')

    def test_3(self):
        self.assertEqual(think('y', ['2 1 x']), 'xy')


def solve():
    s, queries = read()
    result = think(s, queries)
    write(result)


def read():
    s = read_line()
    q = read_int(1)[0]
    queries = []
    for _ in range(q):
        queries.append(read_line())
    return s, queries


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


def think(s, queries):
    buf = collections.deque(list(s))
    reverse = False
    for q in queries:
        splitted = q.split()
        if splitted[0] == '1':
            reverse = not reverse
        elif splitted[0] == '2':
            f = splitted[1]
            c = splitted[2]
            if f == '1':
                if reverse:
                    buf.append(c)
                else:
                    buf.appendleft(c)
            elif f == '2':
                if reverse:
                    buf.appendleft(c)
                else:
                    buf.append(c)
            else:
                raise RuntimeError()
        else:
            raise RunntimeError()
    result = ''.join(list(buf))
    return result[::-1] if reverse else result


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
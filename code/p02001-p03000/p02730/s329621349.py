import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think('akasaka'), 'Yes')

    def test_2(self):
        self.assertEqual(think('level'), 'No')

    def test_3(self):
        self.assertEqual(think('atcoder'), 'No')


def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    return read_line()


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
    if not is_palindrome(s):
        return 'No'
    m = len(s) // 2
    if is_palindrome(s[0:m]) and is_palindrome(s[m + 1:]):
        return 'Yes'
    return 'No'


def write(result):
    print(result)


def is_palindrome(s):
    right = len(s) - 1
    for left in range(len(s)):
        if s[left] == s[right]:
            right -= 1
            continue
        return False
    return True


if __name__ == '__main__':
    # unittest.main()
    solve()
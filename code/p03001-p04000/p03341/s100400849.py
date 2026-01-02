import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    s = list(input())
    cnt_w = s.count('W')
    cnt_e = s.count('E')

    tmp_w = 0
    tmp_e = 0

    ans = []

    for i in range(n):
        if s[i] == 'W':
            tmp_w += 1
        else:
            tmp_e += 1

        if s[i] == 'W':
            ans.append(tmp_w + cnt_e - tmp_e - 1)
        else:
            ans.append(tmp_w + cnt_e - tmp_e)

    print(min(ans))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """5
WEEWW"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
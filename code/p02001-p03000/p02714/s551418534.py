import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    s = input()
    ans = s.count('R') * s.count('G') * s.count('B')

    for i in range(n):
        for j in range(1, (n - 1)//2 + 1, 1):
            if i + 2 * j < n:
                if s[i] != s[i + j] and s[i] != s[i + 2 * j] and s[i + j] != s[i + 2 * j]:
                    ans -= 1

    print(ans)


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
        input = """4
RRGB"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()

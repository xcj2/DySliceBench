import sys
from io import StringIO
import unittest
# import numpy as np

def resolve():
    # s = input()
    n = int(input())
    a = list(map(int, input().split()))
    # l = [list(map(int, input().split())) for _ in range(n)]

    thr = 10 ** 18
    a.sort(reverse=True)
    ans = 1

    if 0 in a:
        ans = 0
    else:
        for a_i in a:
            ans *= a_i

            if ans > thr:
                ans = -1
                break

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
        input = """2
1000000000 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
101 9901 999999000001"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31
4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

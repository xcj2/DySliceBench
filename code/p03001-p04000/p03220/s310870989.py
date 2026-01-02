#
# abcxxx b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 1
    tmpt = float('inf')
    for i in range(N):
        tmp = abs(T-H[i]*0.006-A)
        if tmp == min(tmp, tmpt):
            tmpt = tmp
            ans = i+1
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
12 5
1000 2000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
21 -11
81234 94124 52141"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

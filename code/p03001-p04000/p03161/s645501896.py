import sys
from io import StringIO
import unittest

sys.setrecursionlimit(10 ** 7)


def resolve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    inf = 10 ** 9

    # memo = [inf for _ in range(n)]
    # memo[0] = 0
    # for kk in range(1, min(k, n - 1) + 1):
    #     memo[kk] = abs(h[kk] - h[0])
    #
    # def dp(n):
    #     if n == 0:
    #         return 0
    #     elif memo[n] != inf:
    #         return memo[n]
    #     else:
    #         memo[n] = min([dp(n - kk) + abs(h[n] - h[n - kk]) for kk in range(1, k + 1)])
    #         return memo[n]
    #
    # print(dp(n - 1))

    ans = [inf for _ in range(n)]
    ans[0] = 0

    if n < k:
        k = n - 1

    for kk in range(1, k + 1):
        ans[kk] = abs(h[kk] - h[0])

    for i in range(1, n):
        for kk in range(1, k + 1):
            if i + kk < n:
                ans[i + kk] = min(ans[i + kk], ans[i] + abs(h[i + kk] - h[i]))

    print(ans[-1])

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
        input = """5 3
10 30 40 50 20"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 1
10 20 10"""
        output = """20"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 100
10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """10 4
40 10 20 70 80 10 20 70 80 60"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()

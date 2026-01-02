import sys
from io import StringIO
import unittest

sys.setrecursionlimit(10 ** 7)


def memoize(f):
    cache={}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


def resolve():
    n = int(input())
    h = list(map(int, input().split()))
    inf = n * 10 ** 7

    """
    ボトムアップ型: for loopを使う
    ans = [inf for _ in range(n)]
    ans[0] = 0
    ans[1] = abs(h[1] - h[0])

    for i in range(2, n):
        ans[i] = min(ans[i], ans[i - 1] + abs(h[i] - h[i - 1]), ans[i - 2] + abs(h[i] - h[i - 2]))

    print(ans[-1])
    """

    # トップダウン(メモ再帰型)
    memo = [inf for _ in range(n)]
    # @memoize
    def dp(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return abs(h[1] - h[0])
        elif memo[n] != inf:
            return memo[n]
        else:
            memo[n] = min(dp(n - 1) + abs(h[n] - h[n - 1]), dp(n - 2) + abs(h[n] - h[n - 2]))
            return memo[n]

    print(dp(n - 1))

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
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
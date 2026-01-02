import sys
from io import StringIO
import unittest


def resolve():
    N, W = map(int, input().split())

    wv = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0 for _ in range(W + 1)] for __ in range(N)]

    for i in range(W + 1):
        if i >= wv[0][0]:
            dp[0][i] = wv[0][1]

    # 選ぶ選ばないだと2^n
    for i in range(0, N - 1):
        w = wv[i + 1][0]
        v = wv[i + 1][1]
        for j in range(W + 1):
            if j - w >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
            else:
                dp[i + 1][j] = dp[i][j]

    print(max([l[-1] for l in dp]))



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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
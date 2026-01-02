import sys
from io import StringIO
import unittest

def resolve():
    N, W = map(int, input().split())

    wv = [list(map(int, input().split())) for _ in range(N)]

    # 荷物の個数 * 価値上限 -> 重さ最小化
    # これだとcase2が10**9なので解けない
    inf = 10 ** 10
    max_v = sum([v for w, v in wv])+ 10
    sum_w = sum([w for w, v in wv])

    dp = [[inf for _ in range(max_v + 2)] for __ in range(N + 1)]

    # for i in range(max_v + 2):
    #     dp[0][i] = 0

    for i in range(N + 1):
        dp[i][0] = 0

    # ２つ目の添字を超えないように価値を選んだときの、最小の重み
    # 送るモード
    for i in range(N):
        w = wv[i][0]
        v = wv[i][1]
        for j in range(max_v + 2):
            if j - v >= 0:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)
            else:
                dp[i + 1][j] = dp[i][j]
            # if j - v >= 0:
            #     dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)
            # elif j <= v:
            #     dp[i + 1][j] = min(dp[i][j], w)
            # else:
            #     dp[i + 1][j] = dp[i][j]

    # for d in dp:
    #     print(d)
    # print(W)
    # print([i for d in dp for i, w in enumerate(d) if w <= W])
    print(max([i for d in dp for i, w in enumerate(d) if w <= W]))


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
        input = """1 1000000000
1000000000 10"""
        output = """10"""
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
import sys
from io import StringIO
import unittest
import numpy as np

def resolve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())

    ans = [[-1 for _ in range(n)] for _ in range(3)]

    # 0 -> グーrを出したとき
    # 1 -> ちょきs
    # 2 -> パーp

    for i in range(k):
        for j in range(i, n, k):
            if j < k:
                if t[j] == 'r':
                    ans[0][j] = 0
                    ans[1][j] = 0
                    ans[2][j] = p
                elif t[j] == 's':
                    ans[0][j] = r
                    ans[1][j] = 0
                    ans[2][j] = 0
                elif t[j] == 'p':
                    ans[0][j] = 0
                    ans[1][j] = s
                    ans[2][j] = 0
            else:
                if t[j] == 'r':
                    ans[0][j] = max(ans[1][j - k], ans[2][j - k])
                    ans[1][j] = max(ans[0][j - k], ans[2][j - k])
                    ans[2][j] = max(ans[0][j - k], ans[1][j - k]) + p
                elif t[j] == 's':
                    ans[0][j] = max(ans[1][j - k], ans[2][j - k]) + r
                    ans[1][j] = max(ans[0][j - k], ans[2][j - k])
                    ans[2][j] = max(ans[0][j - k], ans[1][j - k])
                elif t[j] == 'p':
                    ans[0][j] = max(ans[1][j - k], ans[2][j - k])
                    ans[1][j] = max(ans[0][j - k], ans[2][j - k]) + s
                    ans[2][j] = max(ans[0][j - k], ans[1][j - k])

    ans = np.array(ans)
    print(ans[:, (-1*k):].max(axis=0).sum())


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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
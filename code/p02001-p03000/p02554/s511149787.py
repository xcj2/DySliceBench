import sys
from io import StringIO
import unittest

MOD = 1000000007


def resolve():
    N, = map(int, input().split())
    tmp = [[8, 1], [1, 0]]
    nxt = [[0, 0], [0, 0]]
    for i in range(1, N):
        nxt[0][0] = (tmp[0][0] * 8) % MOD
        nxt[0][1] = ((tmp[0][0] * 1) % MOD + (tmp[0][1] * 9) % MOD) % MOD
        nxt[1][0] = ((tmp[0][0] * 1) % MOD + (tmp[1][0] * 9) % MOD) % MOD
        nxt[1][1] = ((tmp[0][1] * 1) % MOD + (tmp[1][0] * 1) % MOD + (tmp[1][1] * 10) % MOD) % MOD
        # print(nxt)
        tmp[0][0]=nxt[0][0]
        tmp[0][1] = nxt[0][1]
        tmp[1][0] = nxt[1][0]
        tmp[1][1] = nxt[1][1]

    print(tmp[1][1]% MOD)


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
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """869121"""
        output = """2511445"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3"""
        output = """54"""
        self.assertIO(input, output)



if __name__ == "__main__":
    resolve()

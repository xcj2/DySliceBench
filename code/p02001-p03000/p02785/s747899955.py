import sys
from io import StringIO
import unittest


def resolve():
    N, K = [int(i) for i in input().split()]
    H = sorted([int(i) for i in input().split()])
    if N <= K:
        H = [0]
    else:
        # if K < (N - K):
        for i in range(K):
            H[len(H) - 1 - i] = 0
        # else:
        #     Hs = []
        #     for i in range(N - K):
        #         Hs.append(H[i])
        #     H = Hs
    print(sum(H))


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
        input = """3 1
4 1 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 9
7 9 3 2 3 8 4 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 0
1000000000 1000000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

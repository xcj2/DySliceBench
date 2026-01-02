# abc160_d.py
import sys
import time
import unittest
from io import StringIO
from collections import defaultdict


def resolve():
    N, X, Y = [int(i) for i in input().split()]
    dd = defaultdict(int)
    X -= 1
    Y -= 1
    for i in range(N):
        for j in range(i + 1, N):
            dd[min(j - i, abs(X - i) + 1 + abs(Y - j),
                   abs(Y - i) + 1 + abs(X - j))] += 1
    for i in range(1, N):
        print(dd[i])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def checkTLE(self, input):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin

    def debugIO(self, input):
        stdin = sys.stdin
        sys.stdin = StringIO(input)
        resolve()
        sys.stdin = stdin

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t), flush=True)

    def test_入力例_1(self):
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_TLE(self):  # TODO:
        input = """2000 2 4"""
        self.checkTLE(input)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()

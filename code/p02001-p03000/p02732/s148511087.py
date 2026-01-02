# abc159_d.py
import sys
import time
import unittest
from io import StringIO
from collections import defaultdict


def resolve():
    N = int(input())
    A = [int(i) for i in input().split()]
    dd = defaultdict(int)
    idx = 0
    cmb = [0] * (N + 1)
    for a in A:
        dd[a] += 1
        idx += 1
        cmb[idx] = cmb[idx - 1] + (idx - 1)
    sum = 0
    for j in dd.keys():
        sum += cmb[dd[j]]
    for i in range(N):
        print(sum - (cmb[dd[A[i]]] - cmb[dd[A[i]] - 1]))


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
        input = """5
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()

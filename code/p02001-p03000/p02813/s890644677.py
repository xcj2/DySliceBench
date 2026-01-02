# abc150_c.py
import sys
import time
import unittest
from io import StringIO
import itertools


def resolve():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [int(i) for i in input().split()]
    a = 0
    b = 0
    i = 0
    for s in itertools.permutations(range(1, N + 1)):
        if a == 0 and tuple(s) == tuple(P):
            a = i + 1
        if b == 0 and tuple(s) == tuple(Q):
            b = i + 1
        i += 1
    print(abs(a - b))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t), flush=True)

    def test_入力例_1(self):
        input = """3
1 3 2
3 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1"""
        output = """17517"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 2 3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()

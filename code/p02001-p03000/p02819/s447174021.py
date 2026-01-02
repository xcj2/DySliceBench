# abc149_c.py
import sys
import time
import unittest
from io import StringIO
import numpy as np


def resolve():
    X = int(input())
    x = np.array([i for i in range(2, -(-X // 2))])
    while 0 in (X % x):
        X += 1
    print(X)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def assertTLE(self, input):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin

    # def test_入力例_n(self):
    #     input = """val"""
    #     self.assertTLE(input)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t), flush=True)

    def test_入力例_1(self):
        input = """20"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99992"""
        output = """100003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()

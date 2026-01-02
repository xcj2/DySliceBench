# abc158_d.py
import sys
import time
import unittest
from io import StringIO


def resolve():
    S = input()
    Q = int(input())
    reverseFlg = False
    preR = ""
    post = ""
    for i in range(Q):
        QQ = input().split()
        if QQ[0] == "1":
            reverseFlg = not reverseFlg
        else:
            if reverseFlg:
                if QQ[1] == "1":
                    post += QQ[2]
                else:
                    preR += QQ[2]
            else:
                if QQ[1] == "1":
                    preR += QQ[2]
                else:
                    post += QQ[2]

    if reverseFlg:
        print(post[::-1] + S[::-1] + preR)
    else:
        print(preR[::-1] + S + post)


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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()

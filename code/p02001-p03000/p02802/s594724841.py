import sys
from io import StringIO
import unittest


def resolve():
    N, M = [int(i) for i in input().split()]
    pp = []
    SS = []
    for _ in range(M):
        p, s = [i for i in input().split()]
        pp.append(int(p))
        SS.append(s)
    AC = 0
    WA = 0
    WAtmp = {}
    flgs = [False] * N
    for i in range(M):
        if not flgs[pp[i] - 1]:
            if SS[i] == "AC":
                AC += 1
                flgs[pp[i] - 1] = True
                if pp[i] - 1 in WAtmp.keys():
                    WA += WAtmp[pp[i] - 1]
            else:
                if pp[i] - 1 in WAtmp.keys():
                    WAtmp[pp[i] - 1] += 1
                else:
                    WAtmp[pp[i] - 1] = 1

    print(AC, WA)


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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)

    def test_入力例_n(self):
        input = """3 5
1 WA
1 AC
2 WA
2 AC
3 WA"""
        output = """2 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

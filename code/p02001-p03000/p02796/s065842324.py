import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    XL = [list(map(int, input().split())) for _ in range(N)]
    XL_re = [[xl[0] - xl[1], xl[0] + xl[1]] for xl in XL]
    XL_re = sorted(XL_re, key=lambda x: x[1])

    cnt = 0
    for i, xl in enumerate(XL_re):
        if i == 0:
            tmp = xl[1]
            cnt += 1
        else:
            if tmp <= xl[0]:
                tmp = xl[1]
                cnt += 1
    print(cnt)


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
        input = """4
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()


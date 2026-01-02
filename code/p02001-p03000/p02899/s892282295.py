import sys
from io import StringIO
import unittest

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
        input = """3
2 3 1"""
        output = """3 1 2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """1 2 3 4 5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
8 2 7 3 4 5 6 1"""
        output = """8 2 4 5 6 7 3 1"""
        self.assertIO(input, output)
def resolve():
    N=int(input())
    A=[int(i) for i in input().split()]
    B=[[A[i],i+1] for i in range(N)]

    B.sort(key=lambda x: x[0])

    C=[str(i[1]) for i in B]
    print(" ".join(C))


if __name__ == "__main__":
    resolve()
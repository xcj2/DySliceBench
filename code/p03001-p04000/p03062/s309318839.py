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
-10 5 -4"""
        output = """19"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
10 -4 -8 -11 3"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """11
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000"""
        output = """10000000000"""
        self.assertIO(input, output)
def resolve():
    N=int(input())
    A=[int(i) for i in input().split()]
    d2=sum([1 if i<0 else 0 for i in A])%2
    B=[abs(i) for i in A]
    bs=sum(B)
    if d2==0:
        print(bs)
    else:
        print(bs-2*min(B))

if __name__ == "__main__":
    resolve()
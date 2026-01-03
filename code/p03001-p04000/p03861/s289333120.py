import sys
import math

def resolve():
        input = sys.stdin.readline
        a,b,x=map(int,input().rstrip().split())

        ax=(a-1)//x
        bx=b//x

        ans=bx-ax
        ans=math.floor(ans)
        print(ans)
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
        input = """4 8 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """0 5 1"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """9 9 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 1000000000000000000 3"""
        output = """333333333333333333"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
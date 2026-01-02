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
        input = """30 100"""
        output = """100"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """12 100"""
        output = """50"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """0 100"""
        output = """0"""
        self.assertIO(input, output)
def resolve():
        (A,B)=(int(i) for i in input().split())
        if A>=13:
                print(B)
        elif A>=6:
                print(int(B/2))
        else:
                print(0)
        

if __name__ == "__main__":
    resolve()

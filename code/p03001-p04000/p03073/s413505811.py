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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)
def resolve():
    S=[int(i) for i in input()]
    X=sum([1 if i%2 != S[i] else 0 for i in range(len(S))])
    Y=sum([1 if S[i] != (i+1)%2 else 0 for i in range(len(S))])
    print(min(X,Y))
if __name__ == "__main__":
    resolve()
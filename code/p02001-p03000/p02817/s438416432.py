import sys
input = sys.stdin.readline
S,T=input().rstrip().split()

def resolve():
    print(T+S)

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
        input = """oder atc"""
        output = """atcoder"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """humu humu"""
        output = """humuhumu"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
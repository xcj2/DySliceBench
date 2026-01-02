# coding: utf-8
# Your code here!
# coding: utf-8
import sys
sys.setrecursionlimit(10000000)

#const
# my functions here!
def pin(type=int):
    return map(type,input().rstrip().split())

def resolve():
    A,B=pin()
    ans=0 if (A<B*2) else A-B*2
    print(ans)
"""
#printデバッグ消した？
#前の問題の結果見てないのに次の問題に行くの？
"""
"""
お前カッコ閉じるの忘れてるだろ
"""
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
        input = """12 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """20 15"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """20 30"""
        output = """0"""
        self.assertIO(input, output)

if __name__=="__main__":resolve()
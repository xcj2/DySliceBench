# coding: utf-8
# Your code here!
# coding: utf-8
import sys
sys.setrecursionlimit(10000000)

#const
dxdy=((1,0),(0,1))
# my functions here!
def pin(type=int):
    return map(type,input().rstrip().split())

def resolve():
    s=input()
    cond= s[2]==s[3] and s[4]==s[5]
    print(["No","Yes"][cond])
"""         
#printデバッグ消した？
#前の問題の結果見てないのに次の問題に行くの？
"""
"""
お前カッコ閉じ,るの忘れてるだろ
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
        input = """sippuu"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """iphone"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """coffee"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
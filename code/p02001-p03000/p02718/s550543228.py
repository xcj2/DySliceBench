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
    N,M=pin()
    A=sorted(list(pin()))
    A.reverse()
    p=(sum(A))/(4*M)
    #print(sum(A),A)
    print(["No","Yes"][A[M-1]>=p])
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
        input = """4 1
5 4 2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
380 19 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 3
4 56 78 901 2 345 67 890 123 45 6 789"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()

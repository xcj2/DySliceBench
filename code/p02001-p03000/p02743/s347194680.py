# coding: utf-8
# Your code here!

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
    a,b,c=pin()
    #from math import sqrt
    #cond =(c-a-b)>sqrt(a*b)*2
    #if c<=a+b:"No"
    cond=0
    t=c-(a+b)
    if t>0 and t**2-4*(a*b)>0:
        cond=1
    print(["No","Yes"][cond])

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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__=="__main__":resolve()
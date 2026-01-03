# coding: utf-8
# Your code here!
# coding: utf-8
import sys
sys.setrecursionlimit(200000000)


# my functions here!

#入力

def pin(type=int):
    return map(type,input().rstrip().split())

def resolve():
    N=input()
    n=len(N)//2
    ans=0
    
    for i in range(n):
        if N[0:i]*2==N[0:i*2]:
            ans=max(ans,i*2)
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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)
if __name__=="__main__":resolve()
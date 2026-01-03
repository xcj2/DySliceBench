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
    N,M=pin()
    ans=0
    red=[False]*N
    red[0]=True
    balls=[1]*N
    
    for i in range(M):
        x,y=pin()
        x,y=x-1,y-1
        #ボールの持ち出し
        if red[x]==True:
            red[y]=True
            if balls[x]==1:
                red[x]=False
        balls[x]-=1
        balls[y]+=1    
    print(sum(red))
    
    
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
    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)

if __name__=="__main__":resolve()
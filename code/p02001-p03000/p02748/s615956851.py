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
    A,B,M=pin()
    a=list(pin())
    b=list(pin())
    ans=min(a)+min(b)
    
    for i in range(M):
       x,y,z=pin()
       ans=min(ans,a[x-1]+b[y-1]-z)
    print(ans)
    #print([["NA","YYMM"],["MMYY","AMBIGUOUS"]][cMMYY][cYYMM])
#if __name__=="__main__":resolve()

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
        input = """2 3 1
3 3
3 3 3
1 2 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 1 2
10
10
1 1 5
1 1 10"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 2 1
3 5
3 5
2 2 2"""
        output = """6"""
        self.assertIO(input, output)
if __name__=="__main__":resolve()
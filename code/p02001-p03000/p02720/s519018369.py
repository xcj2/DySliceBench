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
    k,=pin()
    if k<10:
        print(k)
        return
    else:
        from collections import deque as D
        que=D((i,i) for i in range(1,10))
        num=10
        while(1):
            x,y=que.popleft()
            temp=x%10
            subq=[j for j in range(temp-1,temp+2) if j>=0 and j<10]
            #print(subq)
            for q in subq:
                que.append((x*10+q,num))
                if num == k:
                    print(x*10+q)
                    return
                num+=1
    
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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()


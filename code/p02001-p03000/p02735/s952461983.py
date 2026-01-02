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
    

#絶対TLEする！A問題のpython回答はこちら！！！！

def sx(h,w,ans=0):#depth-first? search functionを障害物を消しながら行う
    from collections import deque as DQ
    q=DQ()
    q.append((h,w,ans,0))
    
    flag=0
    while (len(q) >0):
        temp=q.pop()
        s,t,z,flag=temp
        
        if s>=H or t>=W:continue
        #print(maze[s][t])
        if maze[s][t]=="#":
            z+=1-flag
            flag=1
        elif maze[s][t]==".":
            flag=0
        #print((s,t,z))            
        if z<dp[s][t]:
            dp[s][t]=z
            for d in dxdy:
                q.append((s+d[0],t+d[1],z,flag))

def resolve():
    
    global anss ,dp,H,W,maze
    global res
    res=0
    H,W=pin()
    dp=[[(H+W)]*W for _ in range(H)]
    
    maze=tuple(tuple(input())for i in range(H))
    sx(0,0)
    #print(min(anss),len(anss),res)
    print(dp[H-1][W-1])
    

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
        input = """3 3
.##
.#.
##."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
#.
.#"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
..##
#...
###.
###."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5
.#.#.
#.#.#
.#.#.
#.#.#
.#.#."""
        output = """4"""
        self.assertIO(input, output)


if __name__=="__main__":resolve()

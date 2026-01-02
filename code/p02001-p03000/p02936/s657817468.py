### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

sys.setrecursionlimit(50000000)

class check():
    def __init__(self,n,q):
        readline=sys.stdin.readline
        self.tree=[[] for i in range(n)]
        self.ans=[0]*n
        for i in range(n-1):
            a,b=map(int, readline().rstrip().split())
            a-=1
            b-=1
            self.tree[a].append(b)
            self.tree[b].append(a)
        for i in range(q):
            p,x=map(int, readline().rstrip().split())
            p-=1
            self.ans[p]+=x
    def do(self,root,next):
        if root >= 0:
            self.ans[next]+=self.ans[root]
        for a in self.tree[next]:
            if a==root:
                continue
            self.do(next,a)
    def answer(self):
        print(" ".join(map(str,self.ans)))






def resolve():
    readline=sys.stdin.readline

    n,q=map(int, readline().rstrip().split())
    c=check(n,q)
    c.do(-1,0)
    c.answer()

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------
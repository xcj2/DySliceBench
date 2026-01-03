from itertools import permutations
import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline()[:-1]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
int1 = lambda x: int(x) - 1
def MI1(): return map(int1, sys.stdin.readline().split())
def LI1(): return list(map(int1, sys.stdin.readline().split()))
p2D = lambda x: print(*x, sep="\n")
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    def ok(m):
        cnt=0
        for a in aa:
            if a+m<=n-1:continue
            cnt+=(a+m+1)//(n+1)
            if cnt>m:return False
        return True

    n=II()
    aa=LI()
    mx=max(aa)
    cur=0
    b=0
    while 1:
        cur=0
        for i in range(n):
            c=(aa[i]+b+1)//(n+1)
            c=max(c,0)
            aa[i]-=(n+1)*c
            cur+=c
        if cur==0:break
        b+=cur
    for m in range(b,b+10**5):
        if ok(m):break
    print(m)

main()

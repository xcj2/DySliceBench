from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def MF(): return map(float, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    m,n=MI()
    aa=LI()
    ans=0
    if m==2:
        for i,a in enumerate(aa):
            if i%2+1==a:ans+=1
        ans=min(ans,n-ans)
    else:
        cnt=1
        for a0,a1 in zip(aa,aa[1:]):
            if a0==a1:cnt+=1
            else:
                ans+=cnt//2
                cnt=1
        ans+=cnt//2
    print(ans)

main()


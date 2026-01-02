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
    n,t=MI()
    ab=LLI(n)
    ab.sort()
    dp=[-1]*(t+1)
    dp[0]=0
    for a,b in ab:
        for i in range(t-1,-1,-1):
            pre=dp[i]
            if pre==-1:continue
            ni=min(t,i+a)
            dp[ni]=max(dp[ni],pre+b)
    print(max(dp))

main()

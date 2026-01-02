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
    memo={}
    def f(lv,x):
        if lv==0:return 1
        if x==1:return 0
        if x==ss[lv]:return pp[lv]
        if (lv,x) in memo:return memo[lv,x]
        if x<=ss[lv-1]+1:res=f(lv-1,x-1)
        elif x==ss[lv-1]+2:res=pp[lv-1]+1
        else:res=pp[lv-1]+f(lv-1,x-ss[lv-1]-2)+1
        memo[lv,x]=res
        return res

    ss=[1]
    pp=[1]
    for i in range(50):
        ss.append(ss[-1]*2+3)
        pp.append(pp[-1]*2+1)
    #print(ss)
    #print(pp)
    n,x=MI()
    print(f(n,x))



main()

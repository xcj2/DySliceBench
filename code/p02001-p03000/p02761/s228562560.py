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
    def ok(a):
        t=str(a)
        for c,d in zip(t,dd):
            if d!=-1 and int(c)!=d:return False
        return True

    n,m=MI()
    dd=[-1]*n
    for _ in range(m):
        s,c=MI()
        if dd[s-1]!=-1 and dd[s-1]!=c:
            print(-1)
            exit()
        dd[s-1]=c
    if n==1 and dd[0]<1:
        print(0)
        exit()
    for a in range(10**(n-1),10**n):
        if ok(a):
            print(a)
            exit()
    print(-1)

main()

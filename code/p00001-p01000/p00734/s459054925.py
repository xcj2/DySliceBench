import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline()[:-1]
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def MF(): return map(float, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    while 1:
        n,m=MI()
        if n==0:break
        aa=[II() for _ in range(n)]
        sa=sum(aa)
        sb=0
        bb=set()
        for _ in range(m):
            b=II()
            sb+=b
            bb.add(b)
        d=sa-sb
        if d%2:
            print(-1)
            continue
        d//=2
        for a in aa:
            if a-d in bb:
                print(a,a-d)
                break
        else:
            print(-1)

main()


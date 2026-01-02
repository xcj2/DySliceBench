from collections import *
from heapq import *
import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    n,q=MI()
    s=SI()
    cs=[0]*(n+1)
    for i in range(n-1):
        if s[i:i+2]=="AC":cs[i+2]+=1
    for i in range(n):cs[i+1]+=cs[i]
    for _ in range(q):
        l,r=MI()
        l,r=l-1,r-1
        ans=cs[r+1]-cs[l]
        if s[l-1:l+1]=="AC":ans-=1
        print(ans)

main()

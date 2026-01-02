import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=II()
    hp=[]
    for _ in range(n):
        X,L=MI()
        heappush(hp,(X+L,X-L))
    ans=0
    pr=-10**10
    while hp:
        r,l=heappop(hp)
        if l<pr:continue
        ans+=1
        pr=r
    print(ans)

main()
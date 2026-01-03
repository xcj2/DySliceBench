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
    n=II()
    aa=LI()

    l=[0]*3*n
    s=sum(aa[:n])
    hp=aa[:n]
    heapify(hp)
    for i,a in enumerate(aa[n:2*n+1],n):
        l[i]=s
        s+=a
        a=heappushpop(hp,a)
        s-=a

    r=[0]*3*n
    s=0
    hp=[]
    for a in aa[2*n:]:
        s+=a
        heappush(hp,-a)
    for i in range(2*n-1,n-2,-1):
        a=aa[i]
        r[i+1]=s
        s+=a
        a=-heappushpop(hp,-a)
        s-=a
    ans=max(l[i]-r[i] for i in range(n,2*n+1))
    print(ans)

main()

import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    x,y,a,b,c=MI()
    pp=LI()
    qq=LI()
    rr=LI()
    hp=[]
    for p in pp:heappush(hp,(-p,0))
    for q in qq:heappush(hp,(-q,1))
    for r in rr:heappush(hp,(-r,2))
    cnt=[0]*3
    lim=[x,y,10**9]
    ans=0
    while hp and sum(cnt)<x+y:
        d,i=heappop(hp)
        if cnt[i]==lim[i]:continue
        ans-=d
        cnt[i]+=1
    print(ans)



main()
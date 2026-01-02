from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

def main():
    def dfs(u=0,pu=-1):
        ll[u]=len(uu)
        uu.append(u)
        for v in to[u]:
            if v==pu:continue
            dfs(v,u)
        rr[u]=len(uu)

    def sumlr(l,r):
        return bit.sum(r-1)-bit.sum(l-1)

    n=II()
    cc=LI1()
    to=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=MI1()
        to[a].append(b)
        to[b].append(a)
    ll=[-1]*n
    rr=[-1]*n
    uu=[]
    dfs()
    bit=BitSum(n)
    for u in range(n):bit.add(u,1)
    ctou=defaultdict(list)
    for u,c in enumerate(cc):ctou[c].append(u)
    pn=lambda x:x*(x+1)//2
    for c in range(n):
        log=[]
        ans = pn(n)
        for u in sorted(ctou[c],key=lambda x:-ll[x]):
            us=1
            for v in to[u]:
                if ll[v]<ll[u]:continue
                vs=sumlr(ll[v],rr[v])
                ans-=pn(vs)
                us+=vs
            bit.add(ll[u],-us)
            log.append((ll[u],us))
        vs = sumlr(0,n)
        ans -= pn(vs)
        print(ans)
        for i,s in log:bit.add(i,s)

main()
from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

class UnionFind:
    def __init__(self, n):
        self.state = [-1] * n
        # self.size_table = [1] * n
        # cntはグループ数
        # self.cnt = n

    def root(self, u):
        v = self.state[u]
        if v < 0: return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv: return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv: ru, rv = rv, ru
        if du == dv: self.state[ru] -= 1
        self.state[rv] = ru
        # self.cnt -= 1
        # self.size_table[ru] += self.size_table[rv]
        return

def main():
    n=int(input())
    xx=[]
    yy=[]
    for i in range(n):
        x,y=MI()
        heappush(xx,[x,i])
        heappush(yy,[y,i])
    #print(xx,yy)
    ee=[]
    px,pi=heappop(xx)
    while xx:
        x,i=heappop(xx)
        heappush(ee,[x-px,pi,i])
        pi,px=i,x
    py,pi=heappop(yy)
    while yy:
        y,i=heappop(yy)
        heappush(ee,[y-py,pi,i])
        pi,py=i,y
    #print(ee)
    uf=UnionFind(n)
    cnt=0
    ans=0
    while ee:
        d,u,v=heappop(ee)
        if uf.root(u)==uf.root(v):continue
        uf.merge(u,v)
        ans+=d
        cnt+=1
        if cnt==n-1:break
    print(ans)

main()
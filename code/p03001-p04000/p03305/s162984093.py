import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append([v,d])
        self.e[v].append([u,d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def search(self, s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

def main():
    n,m,s,t = LI()
    aa = [LI() for i in range(m)]
    d1 = Dijkstra()
    d2 = Dijkstra()
    for u,v,a,b in aa:
        d1.add(u,v,a)
        d2.add(u,v,b)
    ad = d1.search(s)
    bd = d2.search(t)
    rr = [inf]
    for i in range(n,0,-1):
        tr = ad[i] + bd[i]
        if tr > rr[-1]:
            tr = rr[-1]
        rr.append(tr)

    return '\n'.join(map(lambda x: str(10**15-x), rr[1:][::-1]))


print(main())


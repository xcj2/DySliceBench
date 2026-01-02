import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [tuple(map(int, l.split())) for l in sys.stdin]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    x,y,z,k = LI()
    a = sorted(LI(), reverse=True)
    b = sorted(LI(), reverse=True)
    c = sorted(LI(), reverse=True)
    u = set()
    q = []
    heapq.heappush(q, (-(a[0]+b[0]+c[0]), 0,0,0))
    u.add((0,0,0))
    r = []
    for _ in range(k):
        t,ai,bi,ci = heapq.heappop(q)
        r.append(-t)
        if ai < x-1:
            nk = (ai+1,bi,ci)
            if nk not in u:
                heapq.heappush(q, (-(a[ai+1]+b[bi]+c[ci]), ai+1,bi,ci))
                u.add(nk)
        if bi < y-1:
            nk = (ai,bi+1,ci)
            if nk not in u:
                heapq.heappush(q, (-(a[ai]+b[bi+1]+c[ci]), ai,bi+1,ci))
                u.add(nk)
        if ci < z-1:
            nk = (ai,bi,ci+1)
            if nk not in u:
                heapq.heappush(q, (-(a[ai]+b[bi]+c[ci+1]), ai,bi,ci+1))
                u.add(nk)

    return '\n'.join(map(str, r))

print(main())



import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    h,w = LI()
    a = [[c=='#' for c in S()] for _ in range(h)]

    def search():
        d = collections.defaultdict(lambda: inf)
        s = (0,0)
        d[s] = 1
        q = []
        heapq.heappush(q, (1, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for ni,nj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny = u[0] + ni
                nx = u[1] + nj
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    continue
                if v[(ny,nx)] or a[ny][nx]:
                    continue
                uv = (ny,nx)
                vd = k + 1
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    d = search()
    r = d[(h-1,w-1)]
    if r == inf:
        return -1
    for ai in a:
        for aj in ai:
            if not aj:
                r -= 1

    return -r


print(main())



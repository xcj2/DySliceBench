import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    n,m = LI()
    aa = [LI() for _ in range(m)]
    s,t = LI()
    e = collections.defaultdict(set)
    for a,b in aa:
        e[a].add(b)

    def search(s):
        d = collections.defaultdict(lambda: inf)
        d[(s,0)] = 0
        q = []
        heapq.heappush(q, (0, (s,0)))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True
            uk = (k+1)
            kk = (k+1) % 3

            for uu in e[u[0]]:
                uv = (uu, kk)
                if v[uv]:
                    continue
                if d[uv] > uk:
                    d[uv] = uk
                    heapq.heappush(q, (uk, uv))

        return d

    d = search(s)
    r = d[(t,0)]
    if r == inf:
        return -1

    return r // 3


print(main())


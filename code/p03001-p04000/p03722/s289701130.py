import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m = LI()
    e = collections.defaultdict(list)
    for _ in range(m):
        a,b,c = LI_()
        e[a].append((b,c+1))

    t = [0] * n

    def search(s):
        d = collections.defaultdict(lambda: -inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s, -1))
        v = [{} for _ in range(n)]
        while len(q):
            k, u, mu = heapq.heappop(q)
            if mu in v[u] and v[u][mu] >= -k:
                continue
            if mu in v[u]:
                v[u][mu] = inf
            else:
                v[u][mu] = -k

            for uv, ud in e[u]:
                vd = -k + ud
                if u in v[uv] and v[uv][u] >= vd:
                    continue
                heapq.heappush(q, (-vd, uv, u))

        return v

    d = search(0)
    if max(d[n-1].values()) == inf:
        return 'inf'
    return max(d[n-1].values())


print(main())

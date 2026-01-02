import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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


def main():
    rr = []

    def f(n):
        pa = LI()
        da = LI()
        e = collections.defaultdict(list)
        for i in range(n-1):
            a = i + 2
            b = pa[i]
            d = da[i]
            e[a].append((b,d))
            e[b].append((a,d))
        rf = collections.defaultdict(bool)
        s = None
        for k,v in e.items():
            if len(v) == 1:
                rf[k] = True
            else:
                s = k
        r = 0
        for k,v in e.items():
            for l,d in v:
                if k > l:
                    continue
                if rf[k] or rf[l]:
                    r += d
                else:
                    r += d * 3

        def search(s):
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

                for uv, ud in e[u]:
                    if v[uv] or rf[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        sd = search(s)
        sm = max(sd.values())
        for k,v in sd.items():
            if v == sm:
                s = k
        sd = search(s)
        sm = max(sd.values())

        return r - sm

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())


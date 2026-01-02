import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+9
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
        a = [I() for _ in range(n)]
        t = [(0,0,0)]
        for c in a:
            nt = collections.defaultdict(lambda: inf)
            c1 = c % 1000
            c5 = c % 500
            mc5 = 500 - c5
            for g,k,p in t:
                nt[(g,k)] = p
            if c1 == 0:
                for g,k,p in t:
                    if k >= 500 and nt[(g+1,k-500)] > p + c:
                        nt[(g+1,k-500)] = p + c
            elif c1 == 500:
                for g,k,p in t:
                    if nt[(g+1, k)] > p + c:
                        nt[(g+1, k)] = p + c
            elif c1 < 500:
                for g,k,p in t:
                    if nt[(g+1, k+mc5)] > p + c:
                        nt[(g+1, k+mc5)] = p + c
            else:
                for g,k,p in t:
                    if k + mc5 >= 500 and nt[(g+1,k+mc5-500)] > p + c:
                        nt[(g+1,k+mc5-500)] = p + c
                    if nt[(g, k+mc5)] > p + c:
                        nt[(g, k+mc5)] = p + c
            t = []
            cg = -1
            mk = -1
            mp = inf
            # print('nt',nt)
            for g,k in sorted(nt.keys(), reverse=True):
                p = nt[(g,k)]
                if p == inf:
                    continue
                if cg != g:
                    mp = inf
                    cg = g
                if mk < k or mp > p:
                    t.append((g,k,p))
                    if mk < k:
                        mk = k
                    if mp > p:
                        mp = p
            # print(len(t))
        r = 0
        rp = inf
        for g,k,p in t:
            if r < g or (r==g and rp > p):
                r = g
                rp = p
        return '{} {}'.format(r, rp)

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))


print(main())


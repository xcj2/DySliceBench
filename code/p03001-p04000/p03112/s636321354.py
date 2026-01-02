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


def main():
    n,m,q = LI()
    s = [I() for _ in range(n)]
    t = [I() for _ in range(m)]
    x = [I() for _ in range(q)]

    rr = []
    for y in x:
        r = inf
        si = bisect.bisect(s, y)
        if si > 0:
            z = s[si-1]
            k = y - z
            ti = bisect.bisect(t, z)
            if ti > 0:
                u = k + z - t[ti-1]
                if r > u:
                    r = u
            if ti < m:
                u = k + t[ti] - z
                if r > u:
                    r = u
        if si < n:
            z = s[si]
            k = z - y
            ti = bisect.bisect(t, z)
            if ti > 0:
                u = k + z - t[ti-1]
                if r > u:
                    r = u
            if ti < m:
                u = k + t[ti] - z
                if r > u:
                    r = u

        ti = bisect.bisect(t, y)
        if ti > 0:
            z = t[ti-1]
            k = y - z
            si = bisect.bisect(s, z)
            if si > 0:
                u = k + z - s[si-1]
                if r > u:
                    r = u
            if si < n:
                u = k + s[si] - z
                if r > u:
                    r = u
        if ti < m:
            z = t[ti]
            k = z - y
            si = bisect.bisect(s, z)
            if si > 0:
                u = k + z - s[si-1]
                if r > u:
                    r = u
            if si < n:
                u = k + s[si] - z
                if r > u:
                    r = u

        rr.append(r)

    return '\n'.join(map(str, rr))



print(main())



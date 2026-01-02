import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

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
    n = I()
    ni = 0

    while ni < n:
        ni += 1
        h,w = LI()
        s = [[c for c in S()] for _ in range(h)]
        d = collections.defaultdict(lambda: [inf,-inf,inf,-inf])
        for i in range(h):
            for j in range(w):
                if s[i][j] == '.':
                    continue
                t = d[s[i][j]]
                if t[0] > i:
                    t[0] = i
                if t[1] < i:
                    t[1] = i
                if t[2] > j:
                    t[2] = j
                if t[3] < j:
                    t[3] = j
        f = True
        k = set(d.keys())
        while f:
            f = False
            for t in list(k):
                hi,ha,wi,wa = d[t]
                ff = True
                for i in range(hi,ha+1):
                    for j in range(wi,wa+1):
                        if s[i][j] != t and s[i][j] != '?':
                            ff = False
                            break
                    if not ff:
                        break
                if ff:
                    k.remove(t)
                    f = True
                    for i in range(hi,ha+1):
                        for j in range(wi,wa+1):
                            s[i][j] = '?'
        if not k:
            rr.append('SAFE')
        else:
            rr.append('SUSPICIOUS')

    return '\n'.join(map(str,rr))


print(main())



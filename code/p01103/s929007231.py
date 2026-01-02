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

    def f(d,w):
        aa = [LI() for _ in range(d)]
        r = 0
        for i in range(d-2):
            for j in range(w-2):
                for k in range(i+2,d):
                    for l in range(j+2,w):
                        mi = inf
                        for m in range(i,k+1):
                            t = aa[m][j]
                            if mi > t:
                                mi = t
                            t = aa[m][l]
                            if mi > t:
                                mi = t
                        for m in range(j,l+1):
                            t = aa[i][m]
                            if mi > t:
                                mi = t
                            t = aa[k][m]
                            if mi > t:
                                mi = t
                        s = 0
                        for m in range(i+1,k):
                            for n in range(j+1,l):
                                if mi <= aa[m][n]:
                                    s = -inf
                                    break
                                s += mi - aa[m][n]
                        if r < s:
                            r = s
        return r


    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))

    return '\n'.join(map(str, rr))


print(main())


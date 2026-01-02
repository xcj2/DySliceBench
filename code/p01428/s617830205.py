import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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
    dd = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

    while True:
        b = [[c for c in S()] for _ in range(8)]
        def g(ps,i,j,di,dj):
            if not (0 <= i < 8) or not (0 <= j < 8):
                return
            if b[i][j] == '.':
                return
            if b[i][j] == ps:
                return 0
            tr = g(ps,i+di,j+dj,di,dj)
            if tr is None:
                return
            return tr + 1

        def ff(ps,i,j,di,dj):
            if not (0 <= i < 8) or not (0 <= j < 8):
                return
            if b[i][j] == '.':
                return
            if b[i][j] == ps:
                return 0
            tr = ff(ps,i+di,j+dj,di,dj)
            if tr is None:
                return
            b[i][j] = ps
            return tr + 1

        def f(pf, pp):
            ps = 'o'
            es = 'x'
            if not pf:
                ps = 'x'
                es = 'o'
            mc = 0
            mij = (0,0)
            for i in range(8):
                for j in range(8):
                    if b[i][j] != '.':
                        continue
                    c = 0
                    for di,dj in dd:
                        tc = g(ps,i+di,j+dj,di,dj)
                        if not tc is None:
                            c += tc
                    if mc < c or (mc == c and not pf):
                        mc = c
                        mij = (i,j)

            if mc > 0:
                i,j = mij
                b[i][j] = ps
                for di,dj in dd:
                    ff(ps,i+di,j+dj,di,dj)
                f(not pf, False)
            elif pp:
                return
            else:
                f(not pf, True)

        f(True, False)

        for i in range(8):
            rr.append(''.join(b[i]))
        break

    return '\n'.join(map(str, rr))


print(main())



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

    while True:
        w,h = LI()
        if w == 0 and h == 0:
            break
        a = [[c for c in S()] for _ in range(h)]
        t = [[0]*w for i in range(h)]
        r = 0
        for i in range(h):
            for j in range(w):
                c = a[i][j]
                if not ('0' <= c <= '9'):
                    continue
                d = int(c) + t[i][j] * 10
                if r < d:
                    r = d
                if i < h-1 and t[i+1][j] < d:
                    t[i+1][j] = d
                if j < w-1 and t[i][j+1] < d:
                    t[i][j+1] = d
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())



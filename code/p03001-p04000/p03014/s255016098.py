import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
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


def main():
    n,m = LI()
    a = [[c=='#' for c in S()] for _ in range(n)]
    b = [[0] * m for _ in range(n)]
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        j = 0
        ai = a[i]
        while j < m:
            if ai[j]:
                j += 1
                continue
            k = j+1
            while k < m and not ai[k]:
                k += 1
            s = k - j
            for l in range(j,k):
                b[i][l] = s
            j = k

    for i in range(m):
        j = 0
        while j < n:
            if a[j][i]:
                j += 1
                continue
            k = j+1
            while k < n and not a[k][i]:
                k += 1
            s = k - j
            for l in range(j,k):
                c[l][i] = s
            j = k

    r = 0
    for i in range(n):
        bi = b[i]
        ci = c[i]
        for j in range(m):
            t = bi[j] + ci[j] - 1
            if r < t:
                r = t

    return r


print(main())


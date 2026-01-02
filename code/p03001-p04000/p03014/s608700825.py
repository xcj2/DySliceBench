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
    a = [[c!='.' for c in l] for l in sys.stdin.readlines()] + [[True] * m]
    b = [[None] * n for _ in range(m)]
    for i in range(n):
        j = 0
        ai = a[i] + [True]
        while j < m:
            if ai[j]:
                j += 1
            else:
                k = j+1
                while not ai[k]:
                    k += 1
                s = k - j
                b[j][i] = s
                if k < m:
                    b[k][i] = 0
                j = k

    r = 0
    c = [0] * n
    for j in range(m):
        bj = b[j]
        for i in range(n):
            if bj[i] is None:
                continue
            c[i] = bj[i]
        i = 0
        while i < n:
            if a[i][j]:
                i += 1
            else:
                k = i+1
                while not a[k][j]:
                    k += 1
                t = max(c[i:k]) + k - i
                if r < t:
                    r = t
                i = k

    return r - 1


print(main())


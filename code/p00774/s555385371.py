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
        h = I()
        if h == 0:
            break

        a = [LI() for _ in range(h)]
        f = True
        r = 0
        while f:
            f = False
            d = [[0]*5 for _ in range(h)]
            for i in range(h):
                for j in range(3):
                    if a[i][j] > 0 and a[i][j] == a[i][j+1] and a[i][j] == a[i][j+2]:
                        d[i][j] = 1
                        d[i][j+1] = 1
                        d[i][j+2] = 1
                        f = True
            for i in range(h):
                for j in range(5):
                    if d[i][j] == 1:
                        r += a[i][j]
                        a[i][j] = 0

            for i in range(h-2,-1,-1):
                for j in range(5):
                    if a[i][j] <= 0:
                        continue
                    k = i
                    while k < h-1 and a[k+1][j] == 0:
                        a[k+1][j] = a[k][j]
                        a[k][j] = 0
                        k += 1

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())



import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    a = [[1 if c == '#' else 0 for c in S()] for _ in range(n)]
    b = [n-sum(a[i]) for i in range(n)]

    t = 0
    for i in range(n):
        if not all([a[j][i] == 1 for j in range(n)]):
            t += 1

    if min(b) == 0:
        return t

    if min(b) == n:
        return -1

    r = min(b) + 1 + t
    for i in range(n):
        ai = a[i]
        for j in range(n):
            if ai[j] == 0:
                continue
            if r > b[j] + t:
                r = b[j] + t

    return r


print(main())





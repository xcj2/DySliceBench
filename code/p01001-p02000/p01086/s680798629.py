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
        n = I()
        if n == 0:
            break
        a = [len(S()) for _ in range(n)]

        def f(i):
            t = [5,7,5,7,7]
            ti = 0
            for c in a[i:]:
                if c > t[ti]:
                    return False
                if t[ti] == c:
                    ti += 1
                    if ti == 5:
                        return True
                else:
                    t[ti] -= c
            return False

        r = 0
        for i in range(n):
            if f(i):
                r = i+1
                break

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())



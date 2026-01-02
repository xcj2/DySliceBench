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
    rr = []

    def f(n,l,r):
        a = [I() for _ in range(n)]
        c = 0
        for t in range(l,r+1):
            k = -1
            for i in range(n):
                if t % a[i] == 0:
                    k = i
                    break
            if k < 0:
                k = n
            if k % 2 == 0:
                c += 1

        return c

    while 1:
        n,m,l = LI()
        if n == 0:
            break
        rr.append(f(n,m,l))

    return '\n'.join(map(str, rr))


print(main())


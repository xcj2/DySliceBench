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

    def f(a):
        m = len(a)
        r = []
        if a[0][0] == a[1][0]:
            if a[0][1] < a[1][1]:
                r = [(a[i][0]-a[i+1][0], a[i][1]-a[i+1][1]) for i in range(m-1)]
            else:
                r = [(a[i+1][0]-a[i][0], a[i+1][1]-a[i][1]) for i in range(m-1)]
        else:
            if a[0][0] < a[1][0]:
                r = [(a[i+1][1]-a[i][1], a[i][0]-a[i+1][0]) for i in range(m-1)]
            else:
                r = [(a[i][1]-a[i+1][1], a[i+1][0]-a[i][0]) for i in range(m-1)]
        return tuple(r)

    while True:
        n = I()
        if n == 0:
            break

        a = []
        for _ in range(n+1):
            m = I()
            a.append([LI() for _ in range(m)])

        t = f(a[0])
        r = []
        for i in range(1,n+1):
            if t == f(a[i]) or t == f(a[i][::-1]):
                rr.append(i)

        rr.append('+++++')



    return '\n'.join(map(str, rr))


print(main())



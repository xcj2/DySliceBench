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
def pf(s): return print(s, flush=True)

def main():
    rr = []

    def f(i,n):
        t = [c for c in str(i)]
        if len(t) < n:
            t = t + ['0'] * (n-len(t))
        t.sort()
        a = int(''.join(t))
        b = int(''.join(t[::-1]))
        return b - a

    while True:
        n,l = LI()
        if n == 0 and l == 0:
            break
        d = {}
        d[n] = 0
        i = 1
        while True:
            n = f(n,l)
            if n in d:
                rr.append('{} {} {}'.format(d[n], n, i-d[n]))
                break
            d[n] = i
            i += 1


    return '\n'.join(map(str, rr))


print(main())



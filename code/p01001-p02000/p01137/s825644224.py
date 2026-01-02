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

    while True:
        n = I()
        if n == 0:
            break
        r = n
        for i in range(n):
            t = i**3
            if t > n:
                break
            u = n - t
            s = math.floor(u**0.5)
            v = u - s**2
            tr = i + s + v
            if r > tr:
                r = tr

        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())



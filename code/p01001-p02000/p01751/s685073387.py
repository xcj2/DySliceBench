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
        a,b,c = LI()
        s = set()
        s.add(0)
        t = 0
        r = -1
        for i in range(60):
            while t > c:
                c += 60
            if t <= c <= t+a:
                r = c
                break
            t += a + b

        rr.append(r)
        break

    return '\n'.join(map(str, rr))


print(main())



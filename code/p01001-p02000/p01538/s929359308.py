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
    q = I()
    qi = 0

    while qi < q:
        qi += 1
        n = S()
        r = 0
        while len(n) > 1:
            r += 1
            t = 0
            for i in range(1,len(n)):
                u = int(n[:i]) * int(n[i:])
                if t < u:
                    t = u
            n = str(t)
        rr.append(r)

    return '\n'.join(map(str, rr))


print(main())



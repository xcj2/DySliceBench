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
    n = I()
    c = set([n])
    for k in range(100):
        d = set()
        for t in c:
            ci = -1
            for i in range(100):
                if 6**i > t:
                    ci = i-1
                    break
            d.add(t-6**ci)
            ci = -1
            for i in range(100):
                if 9**i > t:
                    ci = i-1
                    break

            d.add(t-9**ci)
        c = d
        if 0 in d:
            return k+1

    return -1


print(main())


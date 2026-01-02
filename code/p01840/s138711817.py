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
        n,m,t = LI()
        a = [1] * (t+1)
        l = LI()
        for c in l:
            a[c] = 0
        for c in l:
            for ci in range(c+1,min(c+m,t+1)):
                if a[ci] < 1:
                    break
                a[ci] = 0
            for ci in range(c-1,max(-1,c-m),-1):
                if a[ci] < 1:
                    break
                a[ci] = 0
        r = 0
        for i in range(t):
            if a[i] == 1 and a[i+1] == 1:
                r += 1

        rr.append(r)
        break

    return '\n'.join(map(str, rr))


print(main())



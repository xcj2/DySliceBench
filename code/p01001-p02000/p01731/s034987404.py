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
        a = []
        e = collections.defaultdict(list)
        for i in range(n):
            k = I()
            l = S()
            e[k].append(i+1)
            a.append(l)
        f = [None] * n
        def ff(i,d):
            f[i-1] = 1
            r = ['.' * d + a[i-1]]
            for j in e[i]:
                r += ff(j,d+1)
            return r
        for i in range(n):
            if f[i]:
                continue
            rr += ff(i+1,0)

        break



    return '\n'.join(map(str, rr))


print(main())



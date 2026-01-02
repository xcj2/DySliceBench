import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m = LI()
    e = collections.defaultdict(set)
    t = [0] * n
    for _ in range(m):
        a,b = LI_()
        e[a].add(b)
        e[b].add(a)

    q = [0]
    t[0] = 1
    for i in range(n):
        c = q[i]
        tc = t[c]
        for d in e[c]:
            if t[d] == 0:
                t[d] = 3-tc
                q.append(d)
            elif t[d] == tc:
                return n*(n-1) // 2 - m

    a = sum(t) - n

    return a*(n-a) - m


print(main())



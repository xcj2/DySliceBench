import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n,m = LI()
    a = [LI() for _ in range(n)]
    b = [LI() for _ in range(m)]
    r = []
    for ai in a:
        mi = -1
        mm = inf
        for i in range(m):
            bi = b[i]
            t = abs(ai[0]-bi[0]) + abs(ai[1]-bi[1])
            if t < mm:
                mi = i+1
                mm = t
        r.append(mi)

    return '\n'.join(map(str, r))



print(main())

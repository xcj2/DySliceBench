import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
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
        xy = [LI() for _ in range(n)]
        m = I()
        d = []
        for _ in range(m):
            s,t = S().split()
            d.append((s,int(t)))
        b = collections.defaultdict(bool)
        for x,y in xy:
            b[(x,y)] = True
        x = y = 10
        for s,t in d:
            if s == 'N':
                for _ in range(t):
                    y += 1
                    b[(x,y)] = False
            elif s == 'S':
                for _ in range(t):
                    y -= 1
                    b[(x,y)] = False
            elif s == 'W':
                for _ in range(t):
                    x -= 1
                    b[(x,y)] = False
            else:
                for _ in range(t):
                    x += 1
                    b[(x,y)] = False
        if any(b.values()):
            rr.append('No')
        else:
            rr.append('Yes')

    return '\n'.join(map(str, rr))


print(main())



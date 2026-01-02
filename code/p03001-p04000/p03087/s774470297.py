import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n,q = LI()
    s = S()
    lr = [LI() for _ in range(q)]

    cc = [0,0]
    for i in range(n-1):
        t = cc[-1]
        if s[i:i+2] == 'AC':
            t += 1
        cc.append(t)

    rr = []
    for a,b in lr:
        t = cc[b] - cc[a]
        rr.append(t)

    return '\n'.join(map(str, rr))


print(main())



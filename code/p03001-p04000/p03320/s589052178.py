import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    k = I()
    a = set(list(range(1,10)))
    for i in range(1,16):
        for j in range(1,20*i):
            a.add(int('{}{}'.format(j,'9'*i)))
    m = inf
    for c in sorted(list(a))[::-1]:
        t = 0
        n = c
        while n > 0:
            t += n % 10
            n //= 10
        tm = c / t
        if m < tm - eps:
            a.remove(c)
        else:
            m = tm
    l = sorted(list(a))
    return '\n'.join(map(str,l[:k]))


print(main())


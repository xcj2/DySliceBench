import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
    n = I()
    a = LI()
    c1 = collections.defaultdict(int)
    c2 = collections.defaultdict(int)
    c1['.'] = 0
    c2['a'] = 0
    for i in range(n//2):
        c1[a[i*2]] += 1
        c2[a[i*2+1]] += 1
    m = 0
    for k,v in sorted(c1.items(), key=lambda x: [-x[1], x[0]])[:2]:
        for k2,v2 in sorted(c2.items(), key=lambda x: [-x[1], x[0]]):
            if k2 == k:
                continue
            if m < v+v2:
                m = v+v2
                break

    return n - m


print(main())

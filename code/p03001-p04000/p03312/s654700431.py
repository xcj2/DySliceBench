import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
    n = I()
    a = LI()
    b = [a[0]]
    for c in a[1:]:
        b.append(b[-1]+c)
    d = [0] * n
    d[-1] = a[-1]
    for i in range(n-2,-1,-1):
        d[i] = d[i+1] + a[i]

    g = [[] for _ in range(n)]
    g[0] = [0,inf]
    j = 0
    for i in range(1,n):
        t = b[i]
        k = abs((b[i] - b[j]) - b[j])
        while j < i-1 and k > abs((b[i] - b[j+1]) - b[j+1]):
            k = abs((b[i] - b[j+1]) - b[j+1])
            j += 1
        g[i].append(b[j])
        g[i].append(b[i] - b[j])

    g[-1] = [0,inf]
    g[-2] = [0,inf]
    j = n-1
    for i in range(n-2,-1,-1):
        t = d[i]
        k = abs((d[i] - d[j]) - d[j])
        while j > i+1 and k > abs((d[i] - d[j-1]) - d[j-1]):
            k = abs((d[i] - d[j-1]) - d[j-1])
            j -= 1
        g[i-1].append(d[i] - d[j])
        g[i-1].append(d[j])

    r = inf
    for i in range(n):
        t = max(g[i]) - min(g[i])
        if r > t:
            r = t

    return r



print(main())

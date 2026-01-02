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
    l,n = LI()
    x = [I() for _ in range(n)]
    if n == 1:
        return max(x[0], l-x[0])

    ir = [0]
    for c in x:
        ir.append(ir[-1] + c*2)
    jr = [0]
    for c in x[::-1]:
        jr.append(jr[-1] + (l-c)*2)
    jr = jr[::-1]

    r = max(x[-1], l-x[0])
    for i in range(n-1):
        k = (n - i) // 2 + i
        t = 0
        if (n-i) % 2 == 0:
            t += ir[k] - ir[i]
            t += jr[k+1] + l - x[k]
        else:
            t += ir[k] - ir[i] + x[k]
            t += jr[k+1]
        if r < t:
            r = t

    x = [l-c for c in x][::-1]
    tr = ir[::-1]
    ir = jr[::-1]
    jr = tr
    for i in range(n-1):
        k = (n - i) // 2 + i
        t = 0
        if (n-i) % 2 == 0:
            t += ir[k] - ir[i]
            t += jr[k+1] + l - x[k]
        else:
            t += ir[k] - ir[i] + x[k]
            t += jr[k+1]
        if r < t:
            r = t

    return r


print(main())

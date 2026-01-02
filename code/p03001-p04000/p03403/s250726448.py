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
def pf(s): return print(s, flush=True)


def main():
    n = I()
    a = LI()
    s = 0
    t = 0
    for c in a:
        s += abs(t-c)
        t = c
    s += abs(t)

    r = []
    r.append(s - abs(a[0]) - abs(a[0]-a[1]) + abs(a[1]))
    for i in range(1,n-1):
        r.append(s - abs(a[i-1]-a[i]) - abs(a[i]-a[i+1]) + abs(a[i-1]-a[i+1]))
    r.append(s - abs(a[-1]) - abs(a[-1]-a[-2]) + abs(a[-2]))


    return '\n'.join(map(str,r))


print(main())



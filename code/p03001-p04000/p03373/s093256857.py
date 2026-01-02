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
    a,b,c,x,y = LI()
    if a < b:
        a,b = b,a
        x,y = y,x
    r = 0
    if a > c*2:
        r += x * c*2
        y = max(y-x,0)
        x = 0
    if b > c*2:
        r += y * c*2
        y = 0
    if a+b > c*2:
        t = min(x,y)
        r += t * c*2
        x -= t
        y -= t
    r += a * x
    r += b * y


    return r



print(main())


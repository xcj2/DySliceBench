import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def main():
    n = I()
    a = LI()
    t = 0
    c = a[0]
    r = 1
    for b in a[1:]:
        if c == b:
            continue
        if t==0:
            t = c-b
        elif t * (c-b) < 0:
            r += 1
            t = 0

        c = b

    return r


print(main())

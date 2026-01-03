import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

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
    n,a,b,c,d = LI()
    t = n - 1
    s = abs(a-b)
    if s > d * t:
        return 'NO'
    if s >= c * t:
        return 'YES'

    for i in range(1,t):
        k = c * (t-i) - d * i
        if k <= s:
            if (d-c) * t >= s-k:
                return 'YES'
            break
    return 'NO'


print(main())




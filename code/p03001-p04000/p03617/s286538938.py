import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
 
sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9 + 7
 
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
 
 
def main():
    a = sorted(list(zip(LI(),[0.25,0.5,1.0,2.0])), key=lambda x: x[0]/x[1])
    n = I() * 4
    r = 0
    for i in range(4):
        k,t = a[i]
        t = int(t*4)
        if n >= t:
            r += k * (n//t)
            n %= t
 
    return r
 
print(main())
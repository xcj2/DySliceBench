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
    n,p = LI()
    a = LI()

    r = [0] * 5005
    r[0] = 1
    for c in a:
        for i in range(5000,c-1,-1):
            r[i] += r[i-c]

    rr = 0
    for i in range(5005):
        if i%2 == p:
            rr += r[i]

    return rr


print(main())




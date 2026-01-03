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
    s = set()
    a = LI()
    i = 0
    while True:
        if a[0] % 2 == 1 or a[1] % 2 == 1 or a[2] % 2 == 1:
            return i
        i += 1
        k = tuple(a)
        if k in s:
            return -1
        s.add(k)
        a = [a[0]//2+a[1]//2, a[1]//2+a[2]//2, a[0]//2+a[2]//2]


print(main())

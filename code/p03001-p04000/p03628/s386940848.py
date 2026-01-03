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
    n = I()
    s1 = S()
    s2 = S()
    r = 6
    i = 2
    c = 2
    if s1[0] == s2[0]:
        r = 3
        i = 1
        c = 1
    while i < n:
        if s1[i] == s2[i]:
            if c == 1:
                r *= 2
            else:
                pass
            c = 1
            i += 1
        else:
            if c == 1:
                r *= 2
            else:
                r *= 3
            c = 2
            i += 2
        r %= mod

    return r

print(main())


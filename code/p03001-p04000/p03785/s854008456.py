import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n,c,k = LI()
    a = [II() for _ in range(n)]
    a.sort()
    m = a[0]
    t = 1
    r = 0
    for ai in a[1:]:
        if ai > m+k or t == c:
            r += 1
            t = 1
            m = ai
            continue
        t += 1

    if t > 0:
        r += 1
    return r

print(main())

import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n,k = LI()
    a = sorted(LI())
    sa = sum(a)
    if sa < k:
        return n
    if sa - a[0] < k:
        return 0

    mi = 0
    ma = n-1

    def f(m):
        am = a[m]
        if am >= k:
            return True

        t = [False] * (k-am)
        t[0] = True
        tl = len(t)
        for i in range(n):
            if i==m:
                continue
            ai = a[i]
            for j in range(tl-1,-1,-1):
                if not t[j]:
                    continue
                if k <= j+ai:
                    continue
                if j+ai >= tl:
                    return True

                t[j+ai] = True

        return False

    while mi < ma:
        m = (mi+ma) // 2
        if f(m):
            ma = m
        else:
            mi = m+1

    return mi


print(main())

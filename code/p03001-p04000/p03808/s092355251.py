import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
    n = II()
    a = LI()
    nn = n*(n+1)//2
    s = sum(a)
    if s%nn != 0:
        return "NO"
    k = s//nn
    km = k%n
    c = 0
    for i in range(n):
        t = a[i]-a[i-1]
        if t % n != km:
            return "NO"
        if t > k:
            return "NO"
        kt = k-t
        if kt%n != 0:
            return "NO"
        c += kt//n
    if c == k:
        return "YES"
    return 'NO'


print(main())

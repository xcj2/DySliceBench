from sys import stdin
#, setrecursionlimit, stdout
#setrecursionlimit(1000000)
#from collections import deque
#from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
#from heapq import heapify, heappop, heappush, heappushpop, heapreplace
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def si(): return stdin.readline().rstrip()
def lsi(): return list(si())
#mod=1000000007
res=['NET', 'DA']
############# CODE STARTS HERE #############

def bin_search(a, val):
    pos, l, r=0, 0, len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]<=val:
            pos=m+1
            l=m+1
        else:
            r=m-1
    return pos


test_case=1
while test_case:
    test_case-=1


    n, m, k=mi()
    a=li()
    b=li()
    for i in range(1, n):
        a[i]+=a[i-1]
    for i in range(1, m):
        b[i]+=b[i-1]
    ans=0
    a=[0]+a
    for i in range(n+1):
        if a[i]<=k:
            c=bin_search(b, k-a[i])
            ans=max(ans, c+i)
    print(ans)
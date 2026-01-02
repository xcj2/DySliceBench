from sys import stdin
#, setrecursionlimit, stdout
#setrecursionlimit(1000000)
#from collections import deque
from math import sqrt, floor
#, ceil, log, log2, log10, pi, gcd, sin, cos, asin
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


def sieve(x):
    a=[2]*(x+1)
    a[1]=1
    sq=floor(sqrt(x))
    for i in range(2, sq+1):
        if a[i]:
            for j in range(i*i, x+1, i):
                a[j]+=2
            a[i*i]-=1
    return a


test_case=1
while test_case:
    test_case-=1


    n=ii()
    a=sieve(n)
    c=0
    #print(a)
    for i in range(1, n+1):
        c+=i*a[i]
    print(c)
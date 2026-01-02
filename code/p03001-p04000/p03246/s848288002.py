
def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [input().split() for _ in range(n)]
def s4(n):return [[x for x in s] for s in s2(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]
def t3(n):return [tuple(int(x) for x in input().split()) for _ in range(n)]
def p0(b,yes="Yes",no="No"): print(yes if b else no)
# from sys import setrecursionlimit
# setrecursionlimit(1000000)
from collections import Counter,deque,defaultdict
# import itertools
# import math
# import networkx as nx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n=n0()
V=n1()
V0=[V[i] for i in range(n) if i%2==0]
V1=[V[i] for i in range(n) if i%2==1]

c0=list(Counter(V0).items())
c1=list(Counter(V1).items())
c0.sort(key=lambda x:-x[1])
c1.sort(key=lambda x:-x[1])

if c0[0][0]!=c1[0][0]:
    ans=n-c0[0][1]-c1[0][1]
else:
    if len(c0)==1 or len(c1)==1:
        if len(c0)==len(c1)==1:
            ans=n-c0[0][1]
        elif len(c0)==1:
            ans=n-c1[1][1]
        else:
            ans=n-c0[1][1]        
    elif c0[0][1] > c1[0][1]:
        ans=n-c0[0][1]-c1[1][1]
    elif c0[0][1] < c1[0][1]:
        ans=n-c0[1][1]-c1[0][1]
    else:
        if c0[1][1] > c1[1][1]:
            ans=n-c0[1][1]-c1[0][1]
        else:
            ans=n-c0[0][1]-c1[1][1]
print(ans)

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
from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n,k=n1()
X=n1()

x0=bisect_left(X,0)
if x0<n and X[x0]==0:
    k=k-1
    P=X[x0+1:]
    M=X[:x0]
else:
    P=X[x0:]
    M=X[:x0]

if k==0:
    print(0)
else:
    ans1=ans2=ans3=float("inf")
    if len(P)>=k:
        ans1=P[k-1]
    if len(M)>=k:
        ans2=-M[-k]

    for i in range(1,k):
        j=k-i
        if len(P)>=i and len(M)>=j:
            ans3=min(ans3,P[i-1]*2-M[-j],P[i-1]-2*M[-j])
    print(min(ans1,ans2,ans3))
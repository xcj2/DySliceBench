
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
# from collections import Counter,deque,defaultdict
import itertools
import math
# import networkx as nx
from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n=n0()
A=n1()

A2=[A[i-1]-i for i in range(1,n+1)]
A2.sort()

if n%2==1:
    b=A2[n//2]
    ans=sum([abs(A[i-1]-i-b) for i in range(1,n+1)])
else:
    b1=A2[n//2-1]
    b2=A2[n//2]
    ans1=sum([abs(A[i-1]-i-b1) for i in range(1,n+1)])
    ans2=sum([abs(A[i-1]-i-b2) for i in range(1,n+1)])
    ans=min(ans1,ans2)
print(ans)
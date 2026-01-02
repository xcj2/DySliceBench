
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
# import itertools
# import math
# import networkx as nx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n,w=n1()
WV=n3(n)

W=[0]
W.extend([x[0] for x in WV])
V=[0]
V.extend([x[1] for x in WV])

dp=[[0]*(w+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,w+1):
        if j-W[i]>=0:
            dp[i][j]=max(dp[i-1][j-W[i]]+V[i],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
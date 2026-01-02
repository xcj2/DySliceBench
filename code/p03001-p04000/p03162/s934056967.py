
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
n=n0()
ABC=n3(n)
ABC

dp=[[0,0,0] for _ in range(n)]
dp[0]=ABC[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+ABC[i][0]
    dp[i][1]=max(dp[i-1][0],dp[i-1][2])+ABC[i][1]
    dp[i][2]=max(dp[i-1][0],dp[i-1][1])+ABC[i][2]

print(max(dp[-1]))
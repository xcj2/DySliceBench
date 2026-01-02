
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
s=s0()
t=s0()

len_s=len(s)
len_t=len(t)

dp=[[0]*(len_t+1) for _ in range(len_s+1)]
for i in range(len_s):
    for j in range(len_t):
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j]+1)
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])

# print(dp)

#reverse
ans = ""
i = len_s
j = len_t
while (i>0  and j>0):
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans += s[i-1] 
        i -= 1
        j -= 1
print(ans[::-1])
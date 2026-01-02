
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
n,k=n1()
r,s,p=n1()
t=s0()

def win(h):
    if h=="r":return p
    elif h=="s": return r
    else: return s

ans=0
t2=[False]*n
for i in range(k):
#     print(t[i],ans)
    ans+=win(t[i])
    t2[i]=True
for i in range(k,n):
#     print(t[i],t2[i-k],ans)
    if t[i-k]!=t[i] or t2[i-k]==False:
        ans+=win(t[i])
        t2[i]=True
        
print(ans)

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

d=deque([3,5,7])
ans=0
while True:
    a=d.popleft()
    if a>n:
        break
    else:
        s=str(a)
        if s.count("3")>0 and s.count("5")>0 and s.count("7")>0:
            ans+=1
        d.append(10*a+3)
        d.append(10*a+5)
        d.append(10*a+7)
print(ans)
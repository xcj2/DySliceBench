
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
# import networkx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n,m=n1()
A=n2(m)
A.append(n+1)
b=0
d=[0]*(n+1)
d[0]=1
d[1]=1
for i in range(2,n+1):
    d[i]=d[i-1]+d[i-2]

ans=1
for a in A:
    c=a-1-b
    if a==b:
        print(0)
        break
    else:
        ans*=d[c]
        b=a+1
else:
    print(ans%(10**9+7))
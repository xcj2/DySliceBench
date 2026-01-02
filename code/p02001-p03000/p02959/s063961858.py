
def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [input().split() for _ in range(n)]
def s4(n): return [[x for x in s] for s in s2(n)]
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
n=n0()
a=n1()
b=n1()
ans=0

for i in range(n):
    a1,a2,b1=a[i],a[i+1],b[i]
#     print(a,b,ans)
    if a1-b1>=0:
        ans+=b1
    else:
        ans+=a1
        b1-=a1
        a[i+1]-=min(b1,a2)
        ans+=min(b1,a2)
# print(a,b,ans)
print(ans)
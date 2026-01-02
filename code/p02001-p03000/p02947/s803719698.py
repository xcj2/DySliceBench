
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
from collections import Counter,deque,defaultdict
# import itertools
# import math
# import networkx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
n=n0()
s=s2(n)
d=defaultdict(int)

for line in s:
    a=[0]*26
    c=set((Counter(line)).items())
    for t in c:
        a[ord(t[0])-97]=t[1]
    d[tuple(a)]+=1

ans=0
for i in d.values():
    if i>=2:
        ans+=i*(i-1)//2
print(ans)
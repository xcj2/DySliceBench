
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
ab=t3(n-1)

d={i:[] for i in range(1,n+1)}
for a,b in ab:
    d[a].append(b)
    d[b].append(a)

l=list(d.items())
l.sort(key=lambda x:-len(x[1]))
m=len(l[0][1])

d2={line:0 for line in ab}
c={i:[] for i in range(1,n+1)}
for a1,list1 in l:
    color=1
    for b1 in list1:
        if a1>b1:
            a,b=b1,a1
        else:
            a,b=a1,b1
#         print(a,b)
        if d2[(a,b)]!=0:
            continue
        else:
            while color in c[a] or color in c[b]:
                color+=1 
            d2[(a,b)]=color
            c[a].append(color)
            c[b].append(color)
            color+=1
#     print(d2)
print(m)
for line in ab:
    print(d2[line])
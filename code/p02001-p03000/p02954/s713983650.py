
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
from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop
s=s0()
n=len(s)

L=[]
R=[]
for i in range(n):
    if s[i]=="L":
        L.append(i)
    else:
        R.append(i)

ans=[0]*n
for i in range(n):
    if s[i]=="R":
        j=L[bisect_right(L,i)]
        if (j-i)%2==1:
            ans[j-1]+=1
        else:
            ans[j]+=1
    else:
        j=R[bisect_right(R,i)-1]
        if (i-j)%2==1:
            ans[j+1]+=1
        else:
            ans[j]+=1
print(*ans)
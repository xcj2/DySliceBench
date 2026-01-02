
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
import itertools
# import math
# import networkx
# from bisect import bisect_left,bisect_right
# from heapq import heapify,heappush,heappop

n=n0()
X=[]
for i in range(n):
    a=n0()
    x=n3(a)
    X.append(x)

ite=list(itertools.product([0,1],repeat=n))
ite.sort(key=lambda x:sum(x),reverse=True)

s=0
for line in ite[:-1]:
    ans=[i for i in line]
    flag=True
#     print(line)
    for i in range(n):
        if line[i]==1:
            for a,b in X[i]:
#                 print(ans[a-1],a,b)
                if ans[a-1]!=b:
                    flag=False
                    break
            if flag==False:
                break
    if flag==True:
        for j in range(n):
            if ans[j]==1:
                if line[j]!=1:
                    break
        else:
            s=sum(line)
            break
print(s)
            

def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [input().split() for _ in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]
def t3(n):return [tuple(int(x) for x in input().split()) for _ in range(n)]
def p0(b,yes="Yes",no="No"): print(yes) if b else print(no)
# from collections import Counter,deque,defaultdict
# import itertools
# import math
# import networkx
# from bisect import bisect_left,bisect_right
n=n0()
a=[0]
a.extend(n1())

b=[0]
b.extend(n1())
c=[0]
c.extend(n1())

ans=0
for i in range(1,n+1):
    ans+=b[a[i]]
    if i<n:
        if a[i]+1==a[i+1]:
            ans+=c[a[i]]
print(ans)
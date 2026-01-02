
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
b=n1()

a=[b[0],b[-1]]
for i in range(1,n-1):
    a.append(min(b[i-1],b[i]))

print(sum(a))
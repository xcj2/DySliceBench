
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

X=n0()

def primes(n):
    num = [True]*n
    num[0] = num[1] = False
    for i in range(2,int(n**0.5)+1):
        if num[i]:
            for j in range(i**2, n, i):
                num[j] = False
    return [i for i in range(2,n) if num[i]]

sosuu=primes((10**5)+1000)
while True:
    if X in sosuu:
        print(X)
        break
    X+=1
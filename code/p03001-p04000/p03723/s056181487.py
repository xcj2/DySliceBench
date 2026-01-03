from collections import defaultdict, deque
import sys
import heapq
import bisect
import itertools
import queue
import copy
import time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())

def inpl(): return list(map(int, sys.stdin.readline().split()))

def inpl_str(): return list(sys.stdin.readline().split())

def func(a, b, c):
    if a%2 == 1 or b%2 == 1 or c%2 ==1:
        return 0
    if a == b and a == c:
        return -1
    return func((b+c)//2, (c+a)//2, (a+b)//2) + 1

a, b, c= inpl()
ans = func(a, b, c)
print(ans)
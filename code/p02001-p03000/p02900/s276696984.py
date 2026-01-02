from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

[A,B] = inpl()

def gcd(a,b):
    if a < b: return gcd(b,a)
    else: 
        return gcd(b,a%b) if b != 0 else a

ans_dq = deque([1])

c = gcd(A,B)
for i in range(2,int(c**0.5)//1+1):
    add_or_not = 0
    while c%i == 0:
        c = c//i
        add_or_not = 1
    if add_or_not: ans_dq.append(i)
if c != 1: ans_dq.append(c)

ans = len(ans_dq)
print(ans)
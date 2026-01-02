import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

N,X = map(int,(input().split()))

def S(n):
    return 2**(n+2)-3
def P(n):
    return 2**(n+1)-1

def count(n,x):
    if n == 0:
        return P(0)
    else:
        if x == 1:
            return 0
        if 1 < x <= S(n-1)+1:
            return count(n-1,x-1) 
        if x == S(n-1)+2:
            return 1 + count(n-1,x-2)
        if S(n-1)+2 < x <= 2*S(n-1)+2:
            return P(n-1) + 1 + count(n-1,x-2-S(n-1))
        else:
            return P(n-1) + 1 + count(n-1,x-3-S(n-1))

print(count(N,X))
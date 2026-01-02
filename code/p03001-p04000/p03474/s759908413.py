from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def is_num(x):
    if '0' <= x <= '9':
        return True
    return False
def err():
    print('No')
    quit()

a,b = inpl()
s = input()
for i,x in enumerate(s):
    if i == a:
        if x != '-':
            err()
    else:
        if not is_num(x):
            err()
print('Yes')
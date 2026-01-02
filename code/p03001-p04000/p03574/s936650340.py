from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
from bisect import bisect_left,bisect_right
import sys,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def check(x,y):
    res = 0
    for j in dy:
        for i in dx:
            if s[y][x] == '#':
                return '#'
            if x + i >= w or y + j >= h or x + i < 0 or y + j < 0:
                continue
            if s[y+j][x+i] == '#':
                res += 1
    return res
dx = [-1,0,1]
dy = [-1,0,1]
h,w = inpl()
s = [''] * h
for i in range(h):
    s[i] = input()
res = []
for y in range(h):
    L = ''
    for x in range(w):
        L += str(check(x,y))
    res.append(L)
for i in range(h):
    print(res[i])
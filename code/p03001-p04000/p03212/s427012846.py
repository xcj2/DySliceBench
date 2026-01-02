def dfs(s,n):
    if int(s)>n:
        return 0
    cur = 0
    if all(s.count(c) > 0 for c in '753'):
        cur = 1
    for c in "753":
        cur += dfs(s+c,n)
    return cur
def examC():
    N = I()
    ans = dfs("0",N)
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()

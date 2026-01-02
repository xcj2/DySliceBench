from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def err():
    print('No')
    quit()
n,m = inpl()
s = [input() for _ in range(n)]
dx = (0,1,0,-1)
dy = (1,0,-1,0)
for i in range(n):
    for j in range(m):
        if s[i][j] == '#':
            for d in range(4):
                nx = dx[d]+j
                ny = dy[d]+i
                if 0 <= nx < m and 0 <= ny < n:
                    if s[ny][nx] == '#':
                        break
            else:
                err()
print('Yes')
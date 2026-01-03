from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def err():
    print('Impossible')
    quit()
n,m = inpl()
g = [list(input()) for _ in range(n)]
su = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            su += 1 
if g[0][0] == '.' or su != n+m-1:
    err()
for fl in itertools.permutations(range(n+m-2), n-1):
    # print(fl)
    now = [0,0]
    for i in range(n+m-2):
        if i in fl:
            now[0] += 1
        else:
            now[1] += 1
        y,x = now
        if g[y][x] == '.':
            break
    else:
        print('Possible')
        quit()
err()
    
from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

h,w = inpl()
s = [list(input()) for i in range(h)]
cnt = 0
for i in s:
    cnt += i.count('#')
if cnt != h+w-1:
    print('Impossible')
    quit()
for fl in itertools.combinations(range(h+w-2),h-1):
    nx = 0; ny = 0
    for i in range(h+w-2):
        if i in fl:
            ny += 1
        else:
            nx += 1
        if s[ny][nx] == '#':
            continue
        break
    else:
        print('Possible')
        break
else:
    print('Impossible')

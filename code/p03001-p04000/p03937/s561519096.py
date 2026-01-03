from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

h,w = inpl()
s = [list(input()) for i in range(h)]
if s[0][0] != '#':
    print('Impossible')
    quit()
s[0][0] = '.'
for i in itertools.combinations(range(h+w-2),h-1):
    # print(i)
    cnt = [1] * (h+w-2)
    for l in range(h+w-2):
        if l in i:
            cnt[l] = 0 
    # print(cnt)
    t = [['' for k in range(w)] for j in range(h)] 
    for k in range(h):
        for j in range(w):
            tmp = s[k][j]
            t[k][j] = tmp
    nx = ny = 0
    # print('t')
    # print(t)
    # print('s')
    # print(s)
    # print(i)
    for j in cnt:
        if j:
            nx += 1
        else:
            ny += 1
        if t[ny][nx] == '#':
            t[ny][nx] = '.'
    for j in t:
        if '#' in j:
            break
    else:
        print('Possible')
        # print(i)
        # print(t)
        break
else:
    print('Impossible')

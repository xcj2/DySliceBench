import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

from collections import deque

H, W = mi()
S = [input() for _ in range(H)]

d = dp2(-1, W, H)
d[0][0] = 1
que = deque([[0, 0]])

h = [1, 0, -1, 0]
v = [0, -1, 0, 1]

while que != deque():
    i, j = que.popleft()
    for x in range(4):
        di, dj = h[x], v[x]
        if 0 <= i+di < H and 0 <= j+dj < W:
            if S[i+di][j+dj] !='#' and d[i+di][j+dj] == -1:
                d[i+di][j+dj] = d[i][j] + 1
                que.append([i+di, j+dj])

if d[H-1][W-1] == -1:
    print('-1')
else:
    ans = H*W - d[H-1][W-1] - sum([S[i].count('#') for i in range(H)])
    print(ans)
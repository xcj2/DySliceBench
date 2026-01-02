import math
import time
import pprint
import sys
from collections import deque
pp = pprint.PrettyPrinter(width = 30)
sys.setrecursionlimit(10**7)
INF = 10 ** 18
def MI(): return map(int, sys.stdin.readline().split())
def IS(): return input()
def bfs(q):
    # かかる歩数
    require = [[0 for i in range(w)] for j in range(h)]
    # 訪れたかどうか
    check = [[0 for i in range(w)] for j in range(h)]
    x_diff = [-1, 0, 1, 0]
    y_diff = [0, 1, 0, -1]
    while len(q) != 0:
        tmp_y, tmp_x = q.popleft()
        # print(tmp_y, tmp_x)
        for i in range(4):
            next_y = tmp_y + y_diff[i]
            next_x = tmp_x + x_diff[i]
            if ( 0 <= next_x <= w-1 
                    and 0 <= next_y <= h-1 
                    and check[next_y][next_x] == 0 
                    and a[next_y][next_x] != '#'):
                check[next_y][next_x] = 1 
                require[next_y][next_x] = require[tmp_y][tmp_x] + 1
                q.append([next_y, next_x])
                # pp.pprint(check)
    return require


h, w = MI()
a = [IS() for _ in range(h)]
# start = time.time()
# h, w = 1000, 1000
# a = ['#.#.' * (w//4) for _ in range(h)]
out = 0
que = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            que.append([i,j])
# print(que)

ans = bfs(que)

for i in range(h):
    for j in range(w):
        out = max(out,ans[i][j])

# print(time.time() - start)
print(out)

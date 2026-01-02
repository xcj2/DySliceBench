import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from collections import deque
inf = 10**18
H, W, K = mapint()
y1, x1, y2, x2 = mapint()
query = [list(str(input())) for _ in range(H)]
dirc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

checked = [[-1]*W for _ in range(H)]
checked[y1-1][x1-1] = 0

queue = deque([(y1-1, x1-1)])
def bfs(queue):
    while queue:
        y, x = queue.popleft()
        if y==y2-1 and x==x2-1:
            return checked[y][x]
        for dy, dx in dirc:
            for i in range(1, K+1):
                ny, nx = y+(dy*i), x+(dx*i)
                if ny>=H or ny<0 or nx>=W or nx<0:
                    continue
                if query[ny][nx]=='@':
                    break
                if checked[ny][nx]<0:
                    checked[ny][nx] = checked[y][x]+1
                    queue.append((ny, nx))
                elif checked[ny][nx]<=checked[y][x]:
                    break
    return -1

print(bfs(queue))

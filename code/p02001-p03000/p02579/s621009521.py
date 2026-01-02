from sys import stdin
from queue import Queue
from math import ceil
inp = lambda : stdin.readline().strip()

X = [0,1,0,-1]
Y = [-1,0,1,0]
def isValid(x,y):
    if x >= 0 and y >= 0 and x < h  and y < w:
        return True
    return False


def dfs_iter(x,y):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        if isValid(x,y) and visited[x][y] == -1 and  maze[x][y] != '#':
            visited[x][y] = curr
            for i,j in zip(X,Y):
                if isValid(x+i,y+j) and visited[x+i][y+j] == -1  and maze[x+i][y+j] != '#':
                    stack.append((x+i,y+j))
def bfs(n):
    stack = Queue()
    stack.put(n)
    depths = Queue()
    depths.put(0)
    ans = 10**9 + 7
    while not stack.empty():
        node = stack.get()
        depth = depths.get()
        if not visited2[node]:
            visited2[node] = True
            if node == visited[dh-1][dw-1]:
                ans = min(ans,depth)
            for child in adj[node]:
                if not visited2[child]:
                    stack.put(child)
                    depths.put(depth+1)
    if ans == 10**9 + 7:
        return -1
    return ans


h, w = [int(x) for x in inp().split()]
ch,cw = [int(x) for x in inp().split()]
dh, dw = [int(x) for x in inp().split()]
visited  = [[-1]*w for x in range(h)]

maze = []
adj = [set() for i in range(ceil(h*w/2))]
visited2 = [False]*(ceil(h*w/2))
for i in range(h):
    maze.append(list(inp()))

curr = 0
ans = []
for i in range(h):
    for j in range(w):
        if visited[i][j] == -1 and maze[i][j] != '#':
            dfs_iter(i,j)
            curr += 1
for i in range(h):
    for j in range(w):
        if maze[i][j] != '#':
            for k in range(-2,3):
                for l in range(-2,3):
                    if not (k==l and l == 0):
                        if isValid(i+k,j + l) and visited[i][j] != visited[i+k][j+l] and maze[i+k][j+l] != '#':
                            adj[visited[i][j]].add(visited[i+k][j+l])

print(bfs(visited[ch-1][cw-1]))
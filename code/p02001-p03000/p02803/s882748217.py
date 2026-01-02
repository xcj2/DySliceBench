from collections import deque

h, w = [int(v) for v in input().split()]

maze = []
for i in range(h):
    maze.append(list(input()))

def contains(maze, i, j):
    if i < 0 or i >= h:
        return False
    if j < 0 or j >= w:
        return False
    return True

def far(maze, i0, j0):
    q = deque([])

    q.append((i0, j0, 0))

    closed = set()
    closed.add((i0, j0))
    max_dist = 0
    max_p = None
    while len(q) > 0:
        e = q.popleft()
        
        i = e[0]
        j = e[1]
        cost = e[2] + 1
        for n in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni = i + n[0]
            nj = j + n[1]
            nkey = (ni, nj)
            if not contains(maze, ni, nj):
                continue
            if maze[ni][nj] != '.':
                continue
            nkey = (ni, nj)
            if nkey in closed:
                continue
            closed.add(nkey)
            q.append((ni, nj, cost))
            if max_dist < cost:
                max_dist = cost
                max_p = nkey
    return max_p, max_dist
    
def solve(maze):
    max_dist = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '.':
                continue
            p, dist = far(maze, i, j)
            if max_dist < dist:
                max_dist = dist
    return max_dist

print(solve(maze))
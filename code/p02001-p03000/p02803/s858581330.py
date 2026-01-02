def d_maze_master(INF=float('inf')):
    from collections import deque
    H, W = [int(i) for i in input().split()]
    Maze = [list(input()) for _ in range(H)]

    def bfs(start_row, start_col):
        diff = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def is_inside(row, col):
            return 0 <= row < H and 0 <= col < W

        queue = deque([(start_row, start_col)])
        dist = [[INF for _ in range(W)] for _ in range(H)]
        dist[start_row][start_col] = 0
        while queue:
            row, col = queue.pop()
            for dr, dc in diff:
                nr, nc = row + dr, col + dc
                if is_inside(nr, nc) and Maze[nr][nc] != '#' and dist[nr][nc] == INF:
                    queue.appendleft((nr, nc))
                    dist[nr][nc] = dist[row][col] + 1
        return dist

    ans = 0
    for start_row in range(H):
        for start_col in range(W):
            if Maze[start_row][start_col] == '#':
                continue
            dist = bfs(start_row, start_col)
            for row in range(H):
                for col in range(W):
                    if Maze[row][col] != '#':
                        ans = max(ans, dist[row][col])
    return ans

print(d_maze_master())
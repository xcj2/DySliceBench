import collections

INF = 10 ** 5

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W = ZZ()
    Maze = [input() for _ in range(H)]
    D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(sx, sy):
        dist = [[INF] * W for _ in range(H)]
        dist[sx][sy] = 0
        deq = collections.deque()
        deq.append([sx, sy])
        while deq:
            v = deq.popleft()
            for dx, dy in D:
                nx, ny = v[0]+dx, v[1]+dy
                if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == INF and Maze[nx][ny] == '.':
                    dist[nx][ny] = dist[v[0]][v[1]] + 1
                    deq.append([nx, ny])
        return dist[v[0]][v[1]]

    max_d = -1

    for i in range(H):
        for j in range(W):
            if Maze[i][j] == '.': max_d = max(max_d, bfs(i, j))
    print(max_d)

    return

if __name__ == '__main__':
    main()

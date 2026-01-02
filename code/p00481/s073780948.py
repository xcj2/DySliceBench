import sys
import collections
sys.setrecursionlimit(10 ** 8)
INF = 10 ** 7

def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W, N = ZZ()
    field = [input() for _ in range(H)]
    D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(start, goal):
        dist = [[INF] * W for _ in range(H)]
        deq = collections.deque()
        sx, sy = start
        dist[sx][sy] = 0
        deq.append([sx, sy])

        while deq:
            x, y = deq.popleft()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W and field[nx][ny] != 'X' and dist[nx][ny] == INF:
                    dist[nx][ny] = dist[x][y] + 1
                    deq.append([nx, ny])
        return dist[goal[0]][goal[1]]

    factory = [[] for _ in range(N+1)]
    for i in range(H):
        for j in range(W):
            if field[i][j] == 'S': factory[0] = [i, j]
            elif field[i][j] in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                factory[int(field[i][j])] = [i, j]
    ans = 0
    for i in range(N): ans += bfs(factory[i], factory[i+1])
    print(ans)

    return

if __name__ == '__main__':
    main()


import queue


class HW(object):
    def __init__(self, args: tuple):
        self.h = args[0]
        self.w = args[1]


h, w, n = map(int, input().split())
maze = [input() for i in range(h)]

start = HW((0, 0))
now = HW((0, 0))
nxt = HW((0, 0))

cnt = 0
visited = []


def bfs(target: int) -> int:
    global visited, start, h, w
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    q = queue.Queue()
    q.put((start.h, start.w))
    visited[start.h][start.w] = 0

    while not q.empty():
        tmp = q.get()
        now.h, now.w = tmp[0], tmp[1]
        if maze[now.h][now.w] == str(target):
            start = now
            return visited[now.h][now.w]

        for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt.h, nxt.w = now.h + k[0], now.w + k[1]
            if not 0 <= nxt.h < h or not 0 <= nxt.w < w:
                continue
            elif maze[nxt.h][nxt.w] == "X":
                continue
            elif visited[nxt.h][nxt.w] == -1:
                q.put((nxt.h, nxt.w))
                visited[nxt.h][nxt.w] = visited[now.h][now.w] + 1


def main() -> None:
    for j in range(h):
        for i in range(w):
            if maze[j][i] == "S":
                start.h, start.w = j, i

    for i in range(n):
        global cnt
        cnt += bfs(i + 1)
    print(cnt)


if __name__ == "__main__":
    main()


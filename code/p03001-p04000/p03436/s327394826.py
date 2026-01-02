import queue


class HW(object):
    def __init__(self, height: int, width: int):
        self.h = height
        self.w = width


h, w = map(int, input().split())
maze = [input() for i in range(h)]

cnt = 0
visited = [[0] * w for j in range(h)]


def bfs() -> int:
    q = queue.Queue()
    start = HW(0, 0)
    goal = HW(h - 1, w - 1)
    q.put([start.h, start.w])
    visited[start.h][start.w] = 1

    while q.qsize() > 0:
        tmp = q.get()
        now = HW(tmp[0], tmp[1])
        if now.h == goal.h and now.w == goal.w:
            return cnt - visited[now.h][now.w]

        for k in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nxt = HW(now.h + k[0], now.w + k[1])
            if not 0 <= nxt.h < h or not 0 <= nxt.w < w:
                continue
            elif maze[nxt.h][nxt.w] == '#':
                continue
            elif visited[nxt.h][nxt.w] == 0:
                q.put([nxt.h, nxt.w])
                visited[nxt.h][nxt.w] = visited[now.h][now.w] + 1
    return -1


def main() -> None:
    global cnt
    for i in range(h):
        cnt += maze[i].count('.')

    cnt = bfs()
    print(cnt)


if __name__ == "__main__":
    main()

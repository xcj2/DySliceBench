def main():
    from collections import deque

    h, w = map(int, input().split())
    ch, cw = map(lambda x: int(x) - 1, input().split())
    dh, dw = map(lambda x: int(x) - 1, input().split())

    m = [list(input()) for _ in range(h)]
    vis = [[False for _ in range(w + 2)] for _ in range(h + 2)]

    def walk(i, j):
        q = deque()
        q.append((i, j))
        edge = []
        while q:
            y, x = q.popleft()
            if vis[y][x]:
                continue
            vis[y][x] = True
            for s, t in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if not 0 <= y + s <= h - 1 or not 0 <= x + t <= w - 1:
                    continue
                if m[y + s][x + t] == '#':
                    edge.append((y, x))
                    continue
                q.appendleft((y + s, x + t))
        return edge

    def jump(i, j, c):
        q = walk(i, j)
        if vis[dh][dw]:
            return c
        nx = []
        c += 1
        while q:
            y, x = q.pop()
            for s in range(-2, 3):
                for t in range(-2, 3):
                    if not 0 <= y + s <= h - 1 or not 0 <= x + t <= w - 1:
                        continue
                    if vis[y + s][x + t]:
                        continue
                    if m[y + s][x + t] == '#':
                        continue
                    nx += walk(y + s, x + t)
                    if vis[dh][dw]:
                        return c
            if len(q) == 0:
                c += 1
                q = nx
                nx = []

    ans = jump(ch, cw, 0)
    print(ans if ans is not None else -1)


if __name__ == '__main__':
    main()

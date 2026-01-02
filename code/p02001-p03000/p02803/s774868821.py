from collections import deque


def adjacents(r, c):
    if r > 0:
        yield r - 1, c
    if r < h - 1:
        yield r + 1, c
    if c > 0:
        yield r, c - 1
    if c < w - 1:
        yield r, c + 1


def is_road(r, c):
    return s[r][c] == '.'


def bfs(r, c):
    inf = h * w

    q = deque()
    q.append((r, c))

    dist = [[inf] * w for _ in range(h)]
    dist[r][c] = 0

    while q:
        r, c = q.popleft()
        d = dist[r][c]
        for nr, nc in ((nr, nc) for nr, nc in adjacents(r, c) if is_road(nr, nc)):
            if dist[nr][nc] < inf:
                continue
            nd = d + 1
            dist[nr][nc] = nd
            q.append((nr, nc))

    return d


h, w = map(int, input().split())
s = [input() for _ in range(h)]

print(max(bfs(r, c) for r in range(h) for c in range(w) if is_road(r, c)))

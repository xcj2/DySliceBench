class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0
        self.cost = -1

    def __str__(self):
        return str(self.cost)

    def __repr__(self):
        return str(self.cost)


def show(points):
    for row in points:
        print(*row)


def maxp(points):
    mp = 0
    for row in points:
        for cell in row:
            mp = max(cell.cost, mp)
    return mp


h, w = map(int, input().split())
s = ["#" * (w + 2)] + ["#" + input() + "#" for _ in range(h)] + ["#" * (w + 2)]
ans = 0


for sy in range(h):
    for sx in range(w):
        p = [[Point(x, y) for x in range(w)] for y in range(h)]
        next_search = [(sx, sy)]
        p[sy][sx].cost = 0
        while next_search:
            x, y = next_search.pop(0)
            t = p[y][x]
            if t.state == -1:
                continue
            t.state = -1
            if s[y + 1][x + 1] == "#":
                continue
            if s[y + 1][x] == ".":
                u = p[y][x - 1]
                u.cost = t.cost + 1 if u.cost == -1 else min(t.cost + 1, u.cost)
                next_search.append((x - 1, y))
            if s[y + 1][x + 2] == ".":
                u = p[y][x + 1]
                u.cost = t.cost + 1 if u.cost == -1 else min(t.cost + 1, u.cost)
                next_search.append((x + 1, y))
            if s[y][x + 1] == ".":
                u = p[y - 1][x]
                u.cost = t.cost + 1 if u.cost == -1 else min(t.cost + 1, u.cost)
                next_search.append((x, y - 1))
            if s[y + 2][x + 1] == ".":
                u = p[y + 1][x]
                u.cost = t.cost + 1 if u.cost == -1 else min(t.cost + 1, u.cost)
                next_search.append((x, y + 1))
        ans = max(maxp(p), ans)
print(ans)

from collections import namedtuple

Point = namedtuple('Point', ('x', 'y', 'h'))

def main():
    n = int(input())
    points = [read_point() for _ in range(n)]
    print(*solve(points))

def solve(points):
    for p in points:
        if p.h != 0:
            base = p
            break

    for x in range(0, 101 + 1):
        for y in range(0, 100 + 1):
            h = base.h + abs(base.x - x) + abs(base.y - y)
            for p in points:
                ph = max(h - abs(x - p.x) - abs(y - p.y), 0)
                if ph != p.h:
                    break
            else:
                return Point(x, y, h)

def read_point():
    x, y, h = map(int, input().split())
    return Point(x, y, h)

main()

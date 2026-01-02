def main():
    N = int(input())
    x_y_h = [tuple(map(int, input().split())) for _ in range(N)]

    cx, cy, H = solve(x_y_h)
    print(cx, cy, H)


def height(cx, cy, x_y_h):
    for x, y, h in x_y_h:
        if h <= 0:
            continue
        return h + abs(x - cx) + abs(y - cy)
    return 0


def valid(cx, cy, H, x_y_h):
    for x, y, h in x_y_h:
        if h != max(H - abs(x - cx) - abs(y - cy), 0):
            return False
    return True


def solve(x_y_h):
    for cx in range(101):
        for cy in range(101):
            try_H = height(cx, cy, x_y_h)
            if valid(cx, cy, try_H, x_y_h):
                return cx, cy, try_H
    return 0, 0, 0


main()

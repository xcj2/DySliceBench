import sys
input = sys.stdin.readline

def find_root(root, size, x):
    y = root[x]
    if y is None:
        root[x] = x
        size[x] = 1
        return x
    if x == y:
        return y
    z = find_root(root, size, y)
    root[x] = z
    return z


def merge(root, size, cnt, x, y):
    rx = find_root(root, size, x)
    ry = find_root(root, size, y)
    if rx == ry:
        return
    sx = size[rx]
    sy = size[ry]
    if sx > sy:
        root[ry] = rx
        size[rx] += sy
        cnt[rx] += cnt[ry]
    else:
        root[rx] = ry
        size[ry] += sx
        cnt[ry] += cnt[rx]
    return


def main():
    N = int(input())
    U = 10 ** 5
    root_x = [None] * (U + 1)
    root_y = [None] * (U + 1)
    size_x = [0] * (U + 1)
    size_y = [0] * (U + 1)
    cnt_x = [0] * (U + 1)
    cnt_y = [0] * (U + 1)
    x_to_y = [None] * (U + 1)
    y_to_x = [None] * (U + 1)

    for _ in range(N):
        x, y = map(int, input().split())
        rx = find_root(root_x, size_x, x)
        ry = find_root(root_y, size_y, y)
        cnt_x[rx] += 1
        cnt_y[ry] += 1
        if x_to_y[rx] is None:
            x_to_y[rx] = ry
        if y_to_x[ry] is None:
            y_to_x[ry] = rx
        merge(root_y, size_y, cnt_y, x_to_y[rx], ry)
        merge(root_x, size_x, cnt_x, y_to_x[ry], rx)
        x_to_y[root_x[rx]] = root_y[ry]
        y_to_x[root_y[ry]] = root_x[rx]

    ans = 0
    for x in range(1, U + 1):
        if root_x[x] is None:
            continue
        rx = find_root(root_x, size_x, x)
        if x != rx:
            continue
        y = x_to_y[x]
        ry = find_root(root_y, size_y, y)
        sx = size_x[rx]
        sy = size_y[ry]
        cnt = cnt_x[rx]
        ans += sx * sy - cnt
    print(ans)


if __name__ == "__main__":
    main()

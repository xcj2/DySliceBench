def main():
    W, H, N = map(int, input().split())
    xya = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    #f1(W, H, N, xya)
    f2(W, H, N, xya)


def f1(W, H, N, xya):
    rect = [[1] * W for _ in range(H)]

    for x, y, a in xya:
        x_range = range(W)
        y_range = range(H)
        if a == 1:
            x_range = range(x)
        elif a == 2:
            x_range = range(x, W)
        elif a == 3:
            y_range = range(y)
        elif a == 4:
            y_range = range(y, H)

        for i in y_range:
            for j in x_range:
                rect[i][j] = 0

    ans = sum(map(sum, rect))
    print(ans)


def f2(W, H, N, xya):
    x1, y1 = 0, 0
    x2, y2 = W, H

    for x, y, a in xya:
        if a == 1:
            x1 = max(x, x1)
        elif a == 2:
            x2 = min(x, x2)
        elif a == 3:
            y1 = max(y, y1)
        elif a == 4:
            y2 = min(y, y2)

    if x1 > x2 or y1 > y2:
        ans = 0
    else:
        ans = (x2 - x1) * (y2 - y1)

    #print((x1, y1), (x2, y2))
    print(ans)


if __name__ == '__main__':
    main()

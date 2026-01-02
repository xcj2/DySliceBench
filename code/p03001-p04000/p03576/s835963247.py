def main():
    N, K = map(int, input().split())
    x, y = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    f(N, K, x, y)


def f(N, K, x, y):
    ans = abs(max(x) - min(x)) * abs(max(y) - min(y))
    if K == N:
        print(ans)
        return

    def r(x, y, x_start=0, y_start=0):
        for xi in range(x_start, N):
            for yi in range(y_start, N):
                yield x[xi], y[yi], xi, yi

    # for x1, y1 in zip(x, y):
    #     for x2, y2 in zip(x, y):
    # for x1, y1 in r(x, y):
    #     for x2, y2 in r(x, y):
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    for min_x, min_y, xi, yi in r(sorted_x, sorted_y):
        for max_x, max_y, _, _ in r(sorted_x, sorted_y, x_start=xi+1, y_start=yi+1):

            # s = abs(x1-x2) * abs(y1-y2)
            # if s == 0:
            #     continue

            # min_x = min(x1, x2)
            # max_x = max(x1, x2)
            # min_y = min(y1, y2)
            # max_y = max(y1, y2)

            contains_count = 0
            for x3, y3 in zip(x, y):
                if min_x <= x3 <= max_x and min_y <= y3 <= max_y:
                    contains_count += 1
            if contains_count >= K:
                s = (max_x - min_x) * (max_y - min_y)
                ans = min(ans, s)

    print(ans)


if __name__ == "__main__":
    main()

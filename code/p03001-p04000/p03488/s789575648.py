def main():
    """
    Tの命令 組合せ: 2^N_T
    max_N_T: 8000

    |x|,|y|<=8000
    -> (x,y) 組合せ: 10^8 < 16,000^2 < 10^9
    """
    s = input()
    x, y = map(int, input().split())

    f(s, x, y)
    return
    solve(s, x, y)


def f(s, x, y):
    # Fの数をまとめる
    f_counts = [
        len(fs)
        for fs in s.split("T")
    ]
    # 曲がる方向が90°より、x,yに分解
    x_counts = []
    y_counts = []
    for i, count in enumerate(f_counts):
        if i % 2 == 0:
            x_counts.append(count)
        else:
            y_counts.append(count)

    x_dp = [{} for _ in range(len(x_counts))]
    y_dp = [{} for _ in range(len(y_counts) + 1)]
    pos_x = x_counts.pop(0)
    x_dp[0][pos_x] = True
    y_dp[0][0] = True

    for i, count in enumerate(x_counts):
        for pos in x_dp[i].keys():
            x_dp[i + 1][pos + count] = True
            x_dp[i + 1][pos - count] = True
    for i, count in enumerate(y_counts):
        for pos in y_dp[i].keys():
            y_dp[i + 1][pos + count] = True
            y_dp[i + 1][pos - count] = True

    if x_dp[-1].get(x) and y_dp[-1].get(y):
        print("Yes")
    else:
        print("No")


def solve(s, x, y):
    pos_x, pos_y = 0, 0
    dir_x, dir_y = 1, 0
    for q in s:
        if q == "F":
            pos_x += dir_x
            pos_y += dir_y
        else:
            pass

    if (pos_x, pos_y) == (x, y):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

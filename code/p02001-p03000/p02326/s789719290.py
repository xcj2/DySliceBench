def read_tiles(h, w):
    c = []
    for _ in range(h):
        c.append([int(x) for x in input().split()])
    return c


def largest_square(h, w, c):
    ls = 0
    dp = [[None] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = (
                    min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                )
            ls = max(ls, dp[i][j] ** 2)
    return ls

def main():
    h, w = map(int, input().split())
    c = read_tiles(h, w)
    print(largest_square(h, w, c))


main()


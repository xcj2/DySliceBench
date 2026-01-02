class Item(object):
    def __init__(self, value, weight):
        self.v = value
        self.w = weight


n, W = map(int, input().split())
dp = [[-1] * (W + 1) for i in range(n + 1)]
items = [[int(x) for x in input().split()] for j in range(n)]


def rec_dp(i: int, w: int) -> int:
    if dp[i][w] != -1:
        return dp[i][w]

    result = 0
    if i < 0:
        pass
    else:
        item = Item(items[i][0], items[i][1])
        if w - item.w < 0:
            result = rec_dp(i - 1, w)
        else:
            result = max(
                rec_dp(i - 1, w),
                rec_dp(i - 1, w - item.w) + item.v
            )

    dp[i][w] = result
    return result


def main() -> None:
    print(rec_dp(n - 1, W))


if __name__ == "__main__":
    main()


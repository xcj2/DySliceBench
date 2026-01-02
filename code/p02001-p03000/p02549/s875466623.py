import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, k = input_int_list()
    sections = []
    MOD = 998244353
    for _ in range(k):
        li, ri = input_int_list()
        sections.append((li, ri))
    dp = [0] * (n + 1)
    dpsum = [0] * (n + 1)
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, n + 1):
        for li, ri in sections:
            left = i - ri
            right = i - li
            if right < 0:
                continue
            left = max(1, left)
            dp[i] += dpsum[right] - dpsum[left - 1]
            dp[i] %= MOD
        # 累積和の更新を行う
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[n])

    return


if __name__ == "__main__":
    main()

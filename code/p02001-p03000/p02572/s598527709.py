import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = [0] + input_int_list()  # 1-indexed
    ans = 0
    cusum = [0] * (n + 1)
    MOD = (10**9) + 7

    for i in range(1, n + 1):
        cusum[i] = (A[i] + cusum[i - 1]) % MOD

    ans = 0

    for i in range(1, n):
        ans += (A[i] * (cusum[n] - cusum[i]))
        ans %= MOD
    print(ans)
    return


if __name__ == "__main__":
    main()

import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def main():
    N, M = read_values()
    K = []
    for _ in range(M):
        a, _ = read_values()
        T = read_list()
        K.append((a, T))

    dp = [10 ** 8] * (2 ** N + 10)
    dp[0] = 0
    for a, T in K:
        k = 0
        for t in T:
            k += 1 << (t - 1)
        for i in range(2 ** N):
            dp[i | k] = min(dp[i | k], dp[i] + a) 

    res = dp[2 ** N - 1]
    print(res if res != 10 ** 8 else -1)

if __name__ == "__main__":
    main()

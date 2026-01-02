import sys
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    N = input().strip()
    M = len(N)
    K = int(input())

    dp1 = [[0 for _ in range(K + 1)] for __ in range(M)]
    dp2 = [[0 for _ in range(K + 1)] for __ in range(M)]

    dp1[0][0] = 1
    dp1[0][1] = int(N[0]) - 1
    dp2[0][1] = 1

    for i in range(1, M):
        a = int(N[i])
        for k in range(K + 1):
            dp1[i][k] += dp1[i - 1][k]
            if a > 0:
                dp1[i][k] += dp2[i - 1][k]
            
            if a == 0:
                dp2[i][k] = dp2[i - 1][k]
            else:
                if k > 1:
                    dp2[i][k] = dp2[i - 1][k - 1]

        for k in range(1, K + 1):
            dp1[i][k] += 9 * dp1[i - 1][k - 1]
            if a > 0:
                dp1[i][k] += (a - 1) * dp2[i - 1][k - 1]

    print(dp1[M - 1][K] + dp2[M - 1][K])


if __name__ == "__main__":
    main()


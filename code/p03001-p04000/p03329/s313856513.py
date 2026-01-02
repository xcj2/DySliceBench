import sys
def input(): return sys.stdin.readline().rstrip()

def MIN(a, b):
    if a > b:
        return b
    else:
        return a

def main():
    N = int(input())
    yen6 = [6 ** i for i in range(1, 7) if 6 ** i <= N]
    yen9 = [9 ** i for i in range(1, 6) if 9 ** i <= N]

    if N < 6:
        print(N)
        exit()

    dp = [N] * (N + 1)
    for i in range(6):
        dp[i] = i
    for i in range(1, N + 1):
        for j in yen6:
            if i - j < 0:
                break
            dp[i] = MIN(dp[i], dp[i - j] + 1)
        for j in yen9:
            if i - j < 0:
                break
            dp[i] = MIN(dp[i], dp[i - j] + 1)
    print(dp[N])

if __name__ == '__main__':
    main()

M = 10 ** 9 + 7

def main():
    h, w, k = map(int, input().split())
    k -= 1

    init_fib(w)

    dp = [[None for _ in range(w)] for _ in range(h + 1)]
    for i in range(w):
        dp[0][i] = 0
    dp[0][k] = 1

    for i in range(1, h + 1):
        for j in range(w):
            x = 0
            if j != 0 and dp[i-1][j-1] != 0:
                left = j - 1
                right = w - j - 1
                t = fib(left) * fib(right) % M
                x += t * dp[i-1][j-1] % M
            if j + 1 < w and dp[i-1][j+1] != 0:
                left = j
                right = w - j - 2
                t = fib(left) * fib(right) % M
                x += t * dp[i-1][j+1] % M

            if dp[i-1][j] != 0:
                left = j
                right = w - j - 1
                t = fib(left) * fib(right) % M
                x += t * dp[i-1][j] % M
            
            dp[i][j] = x % M

    print(dp[h][0])

T = []
def init_fib(n):
    global T
    T.append(1)
    T.append(1)

    for i in range(2, n + 1):
        T.append(T[-1] + T[-2])

def fib(n):
    return T[n]

main()

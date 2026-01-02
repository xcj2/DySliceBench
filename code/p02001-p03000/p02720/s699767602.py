def main():
    K = int(input())
    def isr(x):
        a = x % 10
        x //= 10
        b = x % 10
        while x:
            if abs(a - b) > 1:
                return False
            x //= 10
            a, b = b, x % 10
        return True
    dp = [[0] * 11 for _ in range(15)]
    dp2 = [0] * 15
    dp[0][0] = 1
    t = 0

    def nxt(x):
        if x == 0:
            return [0, 1]
        if x == 9:
            return [8, 9]
        return [x - 1, x, x + 1]

    for j in range(1, 10):
        dp[0][j] = 1
        t += dp[0][j]
        if t == K:
            return j

    for i in range(1, 15):
        dp2[i] = t
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        for j in range(1, 10):
            dp[i][j] = sum(dp[i - 1][j - 1:j + 2])
            if t + dp[i][j] >= K:
                r = j
                K -= t
                for p in reversed(range(i)):
                    t = 0
                    for q in nxt(j):
                        if t + dp[p][q] >= K:
                            K -= t
                            r = r * 10 + q
                            j = q
                            break
                        t += dp[p][q]
                return r
            t += dp[i][j]


print(main())

#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int

def comb(n, k):
    if k > n:
        return 0
    k = min(k, n - k)
    ret = 1
    for i in range(k):
        ret *= n - i
        ret //= i + 1
    return ret

def solve(S: str):
    n = len(S)
    b_total = 0
    b_counts = []
    for c in S:
        b_total += ord(c) - ord('0')
        b_counts.append(b_total)
    dp = [[0] * (b_total + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(min(i + 1, b_total + 1)):
            if b_counts[i] >= j + 1:
                dp[i + 1][j + 1] += dp[i][j]
            if (i + 1) * 2 - b_counts[i] >= (i + 1) - j:
                dp[i + 1][j] += dp[i][j]
    #    print(dp[i])
    #print(dp[n])
    comb = [0] * (n + 1)
    comb[0] = 1
    for i in range(n):
        comb[i + 1] = comb[i] * (n - i) // (i + 1)
    ret = 0
    for b, val in enumerate(dp[n]):
        #ret += val * comb(n, b_total - b)
        if b_total - b >= 0 and b_total - b <= n:
            ret += val * comb[b_total - b]
    print(ret % MOD)
    return

    ##dp[0][0] = 1
    ##for i in range(2 * n):
    ##    for j in range(min(i + 1, b_total + 1)):
    ##        b_max = b_counts[i] if i < n else b_total
    ##        r_max = (i + 1) * 2 - b_max if i < n else 2 * n - b_total
    ##        if b_max >= j + 1:
    ##            dp[i + 1][j + 1] += dp[i][j]
    ##        if r_max >= (i + 1) - j:
    ##            dp[i + 1][j] += dp[i][j]
    ##ret = sum(dp[2 * n])
    ##print(ret % MOD)
    ##return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))
    solve(S)

if __name__ == '__main__':
    main()

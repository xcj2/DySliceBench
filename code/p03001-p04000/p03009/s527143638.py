import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n, h, d = MI()
    sum_fact = 0
    n_fact = 1
    for x in range(1, n + 1):
        n_fact *= x
        sum_fact += n_fact
        n_fact %= md
        sum_fact %= md
    if h==1:
        print(n_fact)
        exit()
    dp = [0] * (h + 1)
    dp[0] = dp[1] = n_fact
    s = 0
    for i in range(2, h + 1):
        if i <= d:
            s += dp[i - 1]
            dp[i] = s * sum_fact + dp[0]
        elif i == d + 1:
            s += dp[i - 1]
            dp[i] = s * sum_fact
        else:
            s += dp[i - 1] - dp[i - 1 - d]
            dp[i] = s * sum_fact
        s %= md
        dp[i] %= md
    print(dp[-1])

main()

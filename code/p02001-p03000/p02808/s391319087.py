import sys

sys.setrecursionlimit(10 ** 6)
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

def main():
    def com(com_n, com_r):
        return fac[com_n] * inv[com_r] * inv[com_n - com_r] % md

    n, k = MI()
    aa = LI()
    # combinationの準備
    md = 10 ** 9 + 7
    n_max = n + 3
    fac = [1] * (n_max + 1)
    inv = [1] * (n_max + 1)
    for i in range(2, n_max + 1): fac[i] = fac[i - 1] * i % md
    inv[n_max] = pow(fac[n_max], md - 2, md)
    for i in range(n_max - 1, 1, -1): inv[i] = inv[i + 1] * (i + 1) % md

    dp = [0] * (n + 1)
    dp[0] = 1
    for a in aa:
        for j in range(n, -1, -1):
            pre = dp[j]
            if pre == 0: continue
            dp[j] = 0
            for dj in range(a + 1):
                nj = j + dj
                if nj > n or a - dj < 0 or n - j < dj: break
                dp[nj] += pre * com(n - j, dj) * com(n - dj, a - dj)
                dp[nj] %= md
        # print(dp)
    print(dp[n])

main()

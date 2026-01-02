import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

fac = [1, 1]     # 元テーブル
f_inv = [1, 1]   # 逆元テーブル
inv = [0, 1]     # 逆元テーブル計算用テーブル

def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod//i)) % mod)
        f_inv.append((f_inv[-1] * inv[-1]) % mod)

def modcmb(n, r, mod):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def main():
    K = int(readline())
    S = readline().strip()
    N = len(S)

    prepare(N + K + 10, MOD)

    ans = 0
    for i in range(K+1):
        ans += modcmb(N-1+i, i, MOD) * pow(25, i, MOD) * pow(26, K-i, MOD) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()

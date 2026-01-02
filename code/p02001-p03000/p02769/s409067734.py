import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

fac = [1, 1]
f_inv = [1, 1]
inv = [0, 1]

def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod//i)) % mod)
        f_inv.append((f_inv[-1] * inv[-1]) % mod)


def modcmb(n, r, mod):
    if n < 0 or r < 0 or r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def main():
    N,K = map(int, readline().split())

    prepare(N, MOD)

    ans = 0
    for i in range(min(N-1, K)+1):
        ans += modcmb(N, i, MOD) * modcmb(N-1, i, MOD)
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()

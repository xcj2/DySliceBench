import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())

mod = 10**9 + 7


class CombMod:

    def __init__(self, N, MOD=10**9 + 7):

        N = N + 1
        inv = [0] * N
        fact = [0] * N
        fact_inv = [0] * N

        inv[0] = 0
        inv[1] = 1
        for n in range(2, N):
            q, r = divmod(MOD, n)
            inv[n] = inv[r] * (-q) % MOD

        fact[0] = 1
        for n in range(1, N):
            fact[n] = n * fact[n - 1] % MOD

        fact_inv[0] = 1
        for n in range(1, N):
            fact_inv[n] = fact_inv[n - 1] * inv[n] % MOD

        self.fact = fact
        self.fact_inv = fact_inv
        self.inv = inv

    def comb(self, n, r, mod=10**9 + 7):
        return self.fact[n] * self.fact_inv[r] % mod * self.fact_inv[n - r] % mod

    def perm(self, n, r, mod=10**9 + 7):
        return self.fact[n] * self.fact_inv[n - r] % mod


def main():

    S = in_n()
    if S < 3:
        print(0)
        exit()

    mod = 10**9 + 7
    div = S // 3

    ans = 0
    comb = CombMod(2 * S)
    for k in range(1, div + 1):
        ans += comb.comb(S - 3 * k + k - 1, S - 3 * k)
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()

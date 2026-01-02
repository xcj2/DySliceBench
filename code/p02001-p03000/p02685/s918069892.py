import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


# 互いに素なx, yについて、a * x + b * y = 1の解の一つを求める。
# 参考：http://www.tbasic.org/reference/old/ExEuclid.html
def extGCD(x, y):
    r = [1, 0, x]
    w = [0, 1, y]

    while w[2] != 1:
        q = r[2] // w[2]
        w_tmp = [r[0] - q * w[0], r[1] - q * w[1], r[2] % w[2]]
        r, w = w, w_tmp

    return w[:2]


# 階乗の逆元は(x!)^(-1) * x=((x-1)!)^(-1)を利用する。
# 1 / a mod m を求める。
def mod_inv(a, m):
    x, _ = extGCD(a, m)
    return (x + m) % m


def main():
    MOD = 998244353

    N, M, K = inpl()
    m1 = {}
    m1[0] = 1
    n_comb = {}
    n_comb[0] = 1
    for i in range(1, N + 1):
        m1[i] = (m1[i - 1] * (M - 1)) % MOD
        n_comb[i] = (n_comb[i - 1] * mod_inv(i, MOD) * (N - i)) % MOD

    ans = 0
    for i in range(K + 1):
        ans = (ans + M * n_comb[i] * m1[N - 1 - i]) % MOD

    print(ans)

    return


if __name__ == '__main__':
    main()

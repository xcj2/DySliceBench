mod = 10 ** 9 + 7
fac_table = [1 for i in range(200001)]
inv_table = [1 for i in range(200001)]


def make_table(h, w):

    for i in range(1, h + w - 1):
        fac_table[i] = fac_table[i - 1] * i % mod
        inv_table[i] = pow(fac_table[i], mod - 2, mod)


def comb(n, r):
    return fac_table[n] * inv_table[n - r] % mod * inv_table[r] % mod


def resolve():
    H, W, A, B = map(int, input().split())
    make_table(H, W)
    print(
        sum(
            [
                comb(H - A - 1 + i, i) * comb(A - 1 + W - i - 1, A - 1) % mod
                for i in range(B, W)
            ]
        )
        % mod
    )

if __name__ == "__main__":
    resolve()
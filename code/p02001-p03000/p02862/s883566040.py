X, Y = map(int, input().split())
mod = 10 ** 9 + 7


# modしながらコンビネーションを求める
def mod_cmb(n, r, mod):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * mod_inverse(q, mod) % mod


# modしたa^bを求める
def mod_pow(a, p, mod):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return a * mod_pow(a, p - 1, mod)
    else:
        return (mod_pow(a, p // 2, mod) % mod) ** 2 % mod


# aで割りたいときはa^(p-2)をかければよい（pは素数かつmodで使うやつ）
def mod_inverse(a, mod):
    return mod_pow(a, (mod - 2), mod)


# 移動1, 2を使う回数
n, m = 0, 0

for i in range(10 ** 6):
    if X - i == (Y - 2 * i) * 2 == 0 or X - i == (Y - 2 * i) * 2 != 0:
        n = i
        m = Y - 2 * n
        break
else:
    print(0)
    exit()

print(mod_cmb(n + m, n, mod))
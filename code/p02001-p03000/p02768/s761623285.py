# AtCoder用のライブラリ
# 参照
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a

n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7


# a ** n mod m
def mod_pow(a, n, m=10 ** 9 + 7):
    res = 1
    while n > 0:
        if n & 1 == 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res


# aの-1乗をmで割ったときの商を求める
def mod_inv(a, m=10 ** 9 + 7):
    b = m
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        c = a
        a = b
        b = c

        u -= t * v
        c = u
        u = v
        v = c
    u %= m
    return u


inv_fact_list = [1]
P_list = [1]


def combination(r):
    if r > len(inv_fact_list) - 1:
        _list_extend(r)
    return inv_fact_list[r] * P_list[r] % MOD


def _list_extend(needed):
    now = len(inv_fact_list)
    while now <= needed:
        P_list.append(P_list[-1] * (n - now + 1) % MOD)
        inv_fact_list.append(inv_fact_list[-1] * mod_inv(now) % MOD)
        now += 1


ans = (mod_pow(2, n) - combination(b) - combination(a) - 1) % MOD

print(ans)
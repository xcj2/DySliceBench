import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces

# 大きい数用


mod = 10**9 + 7
N = 10 ** 6 + 1  # 出力の制限
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)

K = ni()
S = ns()
s_len = len(S)
mod = 10 ** 9 + 7
ans = 0

total = K + s_len

rui = 1

cmb = 1

for i in range(total, s_len - 1, -1):
    # print(total - i + 1)
    ans = (ans + cmb * rui) % mod
    # print(ans)
    rui = (rui * 25) % mod
    cmb = (cmb * i * inverse[total - i + 1]) % mod
print(ans)

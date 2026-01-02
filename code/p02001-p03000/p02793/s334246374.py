from functools import reduce

n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
ans = 0

def gcd(a, b):
    # 大きい方を被除数、小さい方を除数とする
    dividend = max(a, b)
    divider = min(a, b)

    if divider == 0:
        return dividend

    # 最大公約数を見つけるまで繰り返す
    while dividend % divider != 0:
        # 除算を行い、その除数を次回の被除数、剰余を次回の除数として処理を繰り返す
        r = dividend % divider
        dividend = divider
        divider = r

    # 一方がもう一方を割り切れた時点で、その除数を最大公約数とみなせる
    return divider


def lcm(a, b):
    return (a * b) // gcd(a, b)

def modinv(x):
    return pow(x, mod-2, mod)

L = reduce(lcm, a)

for i in range(n):
    # ans += (L // a[i])
    ans += L * modinv(a[i])

print(ans % mod)
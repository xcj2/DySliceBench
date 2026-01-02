import math
n = int(input())
k = int(input())
ans = 0


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def partical(L, K, M):  # L:対象の数の長さ K:0以外の個数 M:最大位の数値
    res = 0
    # 最大位の一つ前の位まで
    if L - K > 1:
        res += combinations_count(L - 1, K) * (9 ** K)
    # 最大位の直近の位まで
    if L > 1 and K > 1:
        res += (M - 1) * combinations_count(L - 1, K - 1) * (9 ** (K - 1))
    # 最大位計算の場合
    if K == 1:
        res += M
    return res


def calcLM(target):
    L = len(str(target))
    M = int(str(target)[0])
    return (L, M)


while k > 0:
    L, M = calcLM(n)
    ans += partical(L, k, M)
    n = n - int(str(n)[0]) * (10 ** (len(str(n))-1))
    k = k - 1

print(ans)
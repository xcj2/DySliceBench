import math
import sys

sys.setrecursionlimit(100000000)
# 動的計画法とmemo化で解く。
N, X = map(int, input().split())
S = list(map(int, input().split()))
S.sort(reverse=True)


def memoize(f):  # メモ化関数
    table = [{} for _ in range(N+1)]

    def func(i, key):
        if key not in table[i]:
            table[i][key] = f(i, key)
        return table[i][key]
    return func


@memoize
def dfs(i, x):
    if i == N:
        return x
    else:
        return dfs(i+1, x % S[i]) + dfs(i+1, x) * (N-i-1)


print(dfs(0, X) % (10**9+7))

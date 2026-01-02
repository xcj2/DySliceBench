import sys

import numpy as np

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


def dfs(A):
    m = min(A[A != 0])  # sortしてるので必ず最小値
    # sub_A = [a % m for a in A[1:]]
    sub_A = A[1:] % m  # 最小値で余り
    ans = np.insert(sub_A[sub_A != 0], 0, m)  # 非ゼロ抽出
    if len(ans) != 1:
        ans = dfs(np.sort(ans))
    return ans


def solve():
    N = ii()
    A = np.array(sorted(il()))
    return dfs(A).item()


if __name__ == "__main__":
    print(solve())

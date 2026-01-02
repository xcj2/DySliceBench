import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def argsort(li, key=None, reverse=False):
    return [i for _, i in sorted(
        [(a, i) for i, a in enumerate(li)], key=(lambda t: key(t[0])) if key else None, reverse=reverse
    )]


N, K, Q = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))


def count(l, r, M):
    # [l, r) から M 以下の数を選べる個数
    ret = 0
    for i in range(l, r):
        ret += A[i] <= M
    return min(r - l - K + 1, ret)


def test(M, lr):
    # M 以下の数を Q 個選べるか
    cnt = 0
    for l, r in lr:
        cnt += count(l, r, M)
        if cnt >= Q:
            return True
    return False


def split(lr, i):
    ret = []
    for l, r in lr:
        if l <= i < r:
            if i - l >= K:
                ret.append((l, i))
            if r - (i + 1) >= K:
                ret.append((i + 1, r))
        else:
            ret.append((l, r))
    return ret


# 座圧して BIT 使えばもっと計算量減らせそう
lr = [(0, N)]

ans = max(A) - min(A)
# 小さい順
idx = argsort(A)
for i in idx:
    # i 番目を最小値とする
    m = A[i]
    if test(m + ans - 1, lr):
        ok = m + ans - 1
        ng = m - 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if test(mid, lr):
                ok = mid
            else:
                ng = mid
        ans = ok - m
    lr = split(lr, i)
    if not lr:
        break
print(ans)

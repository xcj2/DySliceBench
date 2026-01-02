import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


# 条件を満たすかどうか
def is_ok(l, i, key):
    # ここが条件
    if l[i] >= key:
        return True


def binary_seach(l, key) -> int:
    left = -1
    right = len(l)

    while right - left > 1:
        mid = left + (right - left) // 2
        if is_ok(l, mid, key):
            right = mid
        else:
            left = mid

    return right


n = I()
l = LI()
l = sorted(l)
ans = 0
for i in range(n - 2):
    # 三角形のうち一番短い辺
    a = l[i]
    for j in range(i + 1, n - 1):
        # 三角形のうち二番目に短い辺
        b = l[j]
        # 三角形の中で一番大きい辺 かつ
        # a + b より小さい辺 を二分探索で探す
        # a + b 以上の要素の初めのindexを取得
        ind = binary_seach(l, a + b)
        # b 以上の辺のうち、a + b より小さい要素の数を足す
        ans += ind - j - 1
print(ans)

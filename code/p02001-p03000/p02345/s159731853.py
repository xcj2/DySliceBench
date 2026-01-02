import sys

INF = 2**31 - 1

SGM = []
n = 0


def init(_n):

    global SGM, n

    n = 1
    while _n > n:
        n *= 2

    SGM = [INF] * (n * 2)


def update(k, x):

    global SGM, n

    k += n - 1  # セグメント木の index に直す
    SGM[k] = x  # i を更新

    # 先祖を更新
    while k > 0:
        k = (k - 1) // 2
        SGM[k] = min(SGM[k * 2 + 1], SGM[k * 2 + 2])


def find(a, b, k, l, r):
    # 節点k がカバーする左側 : l
    # 節点k がカバーする右側 +1 : r

    # 節点 k のエリア [l, r) が、 [a, b) と交差しない場合
    if r <= a or b <= l:
        return INF

    # [a, b) が k -> [l, r) を完全に含む場合
    if a <= l and r <= b:
        return SGM[k]

    # [l, r) に含まれている場合、一段下を捜索
    vl = find(a, b, k * 2 + 1, l, (l + r) // 2)
    vr = find(a, b, k * 2 + 2, (l + r) // 2, r)
    v = min(vl, vr)

    return v


def main():

    global SGM, n
    n, q = map(int, sys.stdin.readline().rstrip().split())

    init(n)

    for i in range(q):
        com, x, y = map(int, sys.stdin.readline().rstrip().split())

        if com == 0:
            update(x, y)
            # print(SGM[n - 1:-1])
        else:
            v = find(x, y + 1, 0, 0, n)  # 区間のとり方の都合上、 y+1 にする
            # print(SGM[n - 1:-1])
            # print(f"find : [{x},{y}]: {v}")
            print(v)


main()


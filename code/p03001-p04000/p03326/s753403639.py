import sys
def input(): return sys.stdin.readline().strip()


def quickSelect(A, k):
    """
    長さnの配列Aの中からk番目(1-indexed)に小さい値を線形時間で求めるアルゴリズム。
    動作原理は次を参照：http://www.flint.jp/blog/?entry=109
    処理の流れは次を参照：https://naoyat.hatenablog.jp/entry/median-of-medians

    使用例：quickSelect([2,7,1,8,2], 5, 3) => 2
    """
    n = len(A)
    while True:
        B = A
        m = n

        # 1.配列からmedian of mediansにより適切なpivotを選択（25%~75%に収まる）
        while m > 5:
            medians = []
            rem = 0
            for i in range(m // 5):
                sortB = sorted(B[i * 5: (i + 1) * 5])
                medians.append(sortB[2])
            if m % 5 != 0:
                sortB = sorted(B[(m // 5) * 5:])
                medians.append(sortB[(m - (m // 5) * 5) // 2])
                rem = 1
            B = medians
            m = m // 5 + rem
        B.sort()
        pivot = B[m // 2]

        # 2.pivotを軸に大小で左右に分ける
        left = []
        right = []
        left_num = 0
        right_num = 0
        for a in A:
            if a < pivot:
                left.append(a)
                left_num += 1
            elif a > pivot:
                right.append(a)
                right_num += 1
        if left_num < k <= n - right_num:
            return pivot
        elif left_num < k:
            A = right
            k -= (n - right_num)
            n = right_num
        else:
            A = left
            n = left_num


def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    cakes = [(0, 0, 0)]
    for _ in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))

    """
    quickSelectによりO(N)で解ける別解を実装。
    x+y+zやx-y-z等のそれぞれに対してcakesをソートして大きい値から取れば良い。
    """

    ans = 0
    for i in range(8):
        sorted_cakes = []
        for j in range(1, N + 1):
            S = 0
            for k in range(3): # iの立っているビットでx, y, zの符号を管理している！！
                if i & (1 << k):
                    S += cakes[j][k]
                else:
                    S -= cakes[j][k]
            sorted_cakes.append(S)

        # ここでsorted_cakesのM番目に大きな値（＝(N - M + 1)番目に小さな値）をquickSelectで求める
        # あとはその数以上なら評価に加算すれば良い
        val = 0
        bound = quickSelect(sorted_cakes, N - M + 1)
        cnt = 0
        for c in sorted_cakes:
            if c > bound:
                val += c
                cnt += 1
        val += bound * (M - cnt)
        ans = max(ans, val)
    print(ans)


if __name__ == "__main__":
    main()

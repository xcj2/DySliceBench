import sys
from bisect import bisect_right
from math import ceil
def input(): return sys.stdin.readline().strip()

class BIT:

    """
    https://tjkendev.github.io/procon-library/python/range_query/bit.html
    Binary index treeの実装
    1-indexedの配列[a1, a2,...,an]に対して以下のクエリをO(logn)で行う:
        1. aiにxを加える
        2. 区間和 ai + a(i+1) + ... + aj の和を求める
    isom法を使えば、
        1. aiの値を取得する
        2. 区間[i, j]の全ての数にxを加算する
    もO(logN)で行うことができる
    """

    def __init__(self, n):
        """
        添字は1スタート
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def add(self, i, x):
        """
        i>0に対してaiにxを加算(x < 0でもOK)
        """
        if i <= 0 or self.n < i:
            raise ValueError("i should be within 1 to n")
        else:
            self.el[i] += x
            while i <= self.n:
                self.data[i] += x
                i += i & -i

    def sum(self, i):
        """
        添字1からiまでの累積和を求める
        """
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i # i $ (-i)でiの最下位ビットのみ立った値を得る
        return s

    def get(self, i, j=None):
        """
        添字iからjまでの累積和を求める
        j=Noneの場合はaiの値を返す
        """
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i - 1)


def main():
    """
    区間の種類数を答える問題は典型みたい。
    https://hama-du-competitive.hatenablog.com/entry/2016/10/01/001418
    ポイントはクエリをrの昇順に整理しておくこと。
    玉の各種類ごとに、それが最後にどこで出現したかをBITに記録していく。
    """
    N, Q = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    queri = []
    for q in range(Q):
        l, r = map(int, input().split())
        queri.append(r * 10**12 + l * 10**6 + q)
    queri.sort()
    # print("queri={}".format(queri))

    lastAppeared = [0] * (N + 1)  # lastAppeared[x] : 値 x が最後に出現した位置
    r0 = queri[0] // 10**12
    for i, c in enumerate(C):
        if i == 0: continue
        if i > r0: break
        lastAppeared[c] = i
    tree = BIT(N)
    for x in range(1, N + 1):
        if lastAppeared[x] != 0:
            tree.add(lastAppeared[x], 1)

    ans = [0] * Q
    pre_R = r0
    for x in queri:
        r, x = x // 10**12, x % 10**12
        l, q = x // 10**6, x % 10**6
        if r > pre_R:
            for i in range(pre_R + 1, r + 1):
                if lastAppeared[C[i]] != 0:
                    tree.add(lastAppeared[C[i]], -1)
                lastAppeared[C[i]] = i
                tree.add(i, 1)
        ans[q] = tree.get(l, r)
        pre_R = r
        # print("q={}, lastAppeared={}, ans={}".format(q, lastAppeared, ans[q]))

    for a in ans: print(a)

if __name__ == "__main__":
    main()

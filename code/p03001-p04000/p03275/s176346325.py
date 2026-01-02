import sys
def input(): return sys.stdin.readline().strip()

class BIT:

    """
    https://tjkendev.github.io/procon-library/python/range_query/bit.html
    Binary index treeの実装
    配列[a1, a2,...,an]に対して以下のクエリをO(logn)で行う:
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
            print("i should be within 1 to n")
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
            i -= i & -i
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
    N = int(input())
    A = list(map(int, input().split()))

    """
    決め打ち二分探索な匂いがする。
    ans <= Xとするとこれはmedian[l, r] <= XなるものがN * (N + 1) // 4個より多く存在することに同値。
    median[l, r] <= Xなるペア[l, r]の個数は以下の用にして求まる：

    １、所与の数列の各元に対して、それがX以下なら-1、Xより大なら+1に置き換える。
    ２、その数列の累積和をとり、先頭に0を追加。
    ３、この数列の転倒数(i < j s.t.A[i] > A[j])を数えると、その個数がmedian[l, r] <= Xなるものの個数になっている。

    転倒数を求めるには分割統治法かBITを使う方法があるが、前者はソート前の配列をコピーする必要があるので
    計算量的に好ましくない？よって後者で実装する。

    この時数列中の数は正であることと、BITの葉ノードは数列中の数のうち最大のものにすることが要求されるが
    今回の場合累積和をとった数列Bの要素は-N以上N以下なのでN + 1の下駄を履かせれば良い。（N <= 10^5なので初期化は十分間に合う）
    """

    left = 0
    right = 10**9
    while right - left > 1:
        #print("left={}, right={}".format(left, right))
        mid = (left + right) // 2
        B = [0] * (N + 1)
        for i in range(1, N + 1):
            if A[i - 1] <= mid: B[i] = B[i - 1] - 1
            if A[i - 1] > mid: B[i] = B[i - 1] + 1

        # Bの転倒数を求める
        tree = BIT(2 * N + 1) # +Nの下駄を履かせる
        cnt = 0
        for i in range(N + 1):
            tree.add(B[i] + N + 1, 1)
            cnt += tree.get(B[i] + N + 2, 2 * N + 1)
        #print("X={}, B={}, cnt={}".format(mid, B, cnt))

        if cnt > N * (N + 1) // 4: right = mid
        else: left = mid
    print(right)

if __name__ == "__main__":
    main()

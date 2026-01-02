
import math

class SegTreeMax:
    def __init__(self, n):
        m = 1
        while m < n:
            m *= 2
        self.n = m
        self.dat = [0] * (2 * self.n - 1)

    def update(self, k, x):
        k += self.n - 1 # 木上のインデックス
        self.dat[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = max(
                self.dat[2 * k + 1],
                self.dat[2 * k + 2]
            )
    
    def query(self, a, b, k=0, l=0, r=None):
        if not r:
            r = self.n
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.dat[k]
        m = (l + r) // 2
        vl = self.query(a, b, k * 2 + 1, l, m)
        vr = self.query(a, b, k * 2 + 2, m, r)
        return max(vl, vr)


def submit():
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # dpをセグメントツリーで管理
    # dp[hi] = a[i] + max(dp[j]) for j < hi
    sgt = SegTreeMax(n)
    
    for i in range(n):
        d = sgt.query(0, h[i])
        if d > 0:
            sgt.update(h[i] - 1, a[i] + d)
        else:
            sgt.update(h[i] - 1, a[i])
    print(sgt.query(0, n))


if __name__ == "__main__":
    submit()
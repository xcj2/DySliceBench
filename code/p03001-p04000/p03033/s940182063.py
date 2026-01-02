import bisect
 
 
class SegTree:
 
    def __init__(self, n):
        # supposed that n = 2**m
        self.n = n
        self.val = [-1] * (2 * n - 1)
 
    def _update(self, a, b, v, k, l, r):
        # 区間[a, b)上の値をvに更新
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.val[k] = v
        else:
            self._update(a, b, v, 2 * k + 1, l, (l + r) // 2)
            self._update(a, b, v, 2 * k + 2, (l + r) // 2, r)
 
    def query(self, x):
        # ノードxの値を返す
        k = self.n + x - 1
        ret = self.val[k]
        while k > 0:
            k = (k - 1) // 2
            ret = max(ret, self.val[k])
        return ret
 
 
def main():
    N, Q = list(map(int, input().split(' ')))
    work_list = [list(map(int, input().split(' '))) for n in range(N)] 
    # 工事は出発地から遠い順に並べておく
    work_list.sort(key=lambda work: work[2], reverse=True)
    D = [int(input()) for q in range(Q)]
    # 一番最初に引っかかる工事のインデックスを求める
    QQ = 1
    while QQ < Q:
        QQ <<= 1
    tree = SegTree(QQ)
    for w, work in enumerate(work_list):
        s, t, x = work
        # s - x <= d < t - x だと工事に引っかかる
        left = bisect.bisect_left(D, s - x)
        right = bisect.bisect_left(D, t - x)
        tree._update(left, right, w, 0, 0, QQ)
    for q in range(Q):
        w = tree.query(q)
        if w == -1:
            print(-1)
        else:
            print(work_list[w][2])
 
 
if __name__ == '__main__':
    main()
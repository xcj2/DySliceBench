
class StarrySkyTree:
    """ Starry Sky Tree(区間加算・区間最小(大)値取得) """

    def __init__(self, N, func, intv):
        self.intv = intv
        self.func = func
        LV = (N - 1).bit_length()
        self.N0 = 2 ** LV
        self.data = [0] * (2 * self.N0)
        self.lazy = [0] * (2 * self.N0)

    # 伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
    def gindex(self, l, r):
        L = l + self.N0
        R = r + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1

    # 遅延評価の伝搬処理
    def propagates(self, *ids):
        # 1-indexedで単調増加のインデックスリスト
        for i in reversed(ids):
            v = self.lazy[i - 1]
            if not v:
                continue
            self.lazy[2 * i - 1] += v
            self.lazy[2 * i] += v
            self.data[2 * i - 1] += v
            self.data[2 * i] += v
            self.lazy[i - 1] = 0

    def update(self, l, r, x):
        """ 区間[l,r)の値にxを加算 """

        # 1. lazyの値は伝搬させない
        # 2. 区間[l,r)のdata, lazyの値を更新
        L = self.N0 + l
        R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] += x
                self.data[R - 1] += x
            if L & 1:
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                L += 1
            L >>= 1
            R >>= 1
        # 3. 更新される区間を部分的に含んだ区間のdataの値を更新 (lazyの値を考慮)
        for i in self.gindex(l, r):
            self.data[i - 1] = self.func(self.data[2 * i - 1], self.data[2 * i]) + self.lazy[i - 1]

    def query(self, l, r):
        """ 区間[l,r)の最小(大)値を取得 """

        # 1. トップダウンにlazyの値を伝搬
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l
        R = self.N0 + r

        # 2. 区間[l, r)の最小(大)値を求める
        s = self.intv
        while L < R:
            if R & 1:
                R -= 1
                s = self.func(s, self.data[R - 1])
            if L & 1:
                s = self.func(s, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

def resolve():
    N, M = map(int, input().split())
    # 1_index
    Pair = [[] for _ in range(N+1)]
    for _ in range(M):
        l, r, a = map(int, input().split())
        Pair[r].append((l, a))

    seg = StarrySkyTree(N+1, func=max, intv=0)

    for i in range(1, N+1):
        _max = seg.query(0, i)
        seg.update(i, i+1, _max)
        for p in Pair[i]:
            l = p[0]
            a = p[1]
            seg.update(l, i+1, a)

    print(seg.query(0, N+1))

if __name__ == "__main__":
    resolve()

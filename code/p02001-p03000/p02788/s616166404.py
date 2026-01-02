

class LasySegmentTree:
    def __init__(self, size: int, segfunc, lazy_ide_ele=0):
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        self.N0 = 1 << (size - 1).bit_length()
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)

    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
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

    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            self.lazy[2 * idx + 1] = self.segfunc(self.lazy[2 * idx + 1], v)
            self.lazy[2 * idx + 2] = self.segfunc(self.lazy[2 * idx + 2], v)
            self.lazy[idx] = self.lazy_ide_ele

    def update(self, left: int, right: int, x):
        L = self.N0 + left
        R = self.N0 + right

        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = self.segfunc(self.lazy[R - 1], x)
            if L & 1:
                self.lazy[L - 1] = self.segfunc(self.lazy[L - 1], x)
                L += 1
            L >>= 1
            R >>= 1

    def query(self, k: int):
        self.propagates(*self.gindex(k, k + 1))
        return self.lazy[k + self.N0 - 1]



from operator import add
from bisect import bisect_right
def resolve():
    N, D, A = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    X, _ = zip(*AB)


    seg_lazy = LasySegmentTree(N+10, segfunc=add)
    ans = 0
    for i in range(N):
        d = AB[i][1] - seg_lazy.query(i)
        if d <= 0:
            continue
        cnt = -(-d//A)
        ans += cnt
        idx = bisect_right(X, (X[i] + 2*D))
        seg_lazy.update(i, idx, cnt*A)
    print(ans)


if __name__ == "__main__":
    resolve()
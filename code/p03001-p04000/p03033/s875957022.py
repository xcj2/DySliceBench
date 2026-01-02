import sys
input = sys.stdin.readline
from bisect import bisect_left
inf = float('inf')

# 区間更新　一点取得　1-indexed
class SegmentTree:
    def __init__(self, N):
        tmp = 1
        while tmp < N:
            tmp <<= 1
        # self.N : 完全二分木の葉の数(N以上の最小の2べき)
        self.N = tmp
        # 2*self.N - 1 : 完全二分木のノード数
        # 1-indexedで管理するので余分に１つ設ける
        self.Data = [inf for _ in range(2*self.N)]
    
    # [l, r) (0-indexed)
    def update(self, l, r, x):
        # インデックスを補正
        L = l + self.N
        R = r + self.N
        while L < R:
            # 右側なら右側を更新 右上に行く
            # 左側なら更新しない　上に行く
            if L & 1:
                self.Data[L] = min([self.Data[L], x])
                L += 1
            # 右側なら左側を更新　上に行く
            # 左側なら更新しない 上に行く
            if R & 1:
                R -= 1
                self.Data[R] = min([self.Data[R], x])
            L >>= 1; R >>= 1
    
    # k (0-indexed)
    def value(self, k):
        # インデックスを補正
        k += self.N
        res = self.Data[k]
        while k != 1:
            k >>= 1
            res = min(res, self.Data[k])
        return res


N, Q = map(int,input().split())
STX = [list(map(int,input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

st = SegmentTree(Q)
for S, T, X in STX:
    l = bisect_left(D, S-X)
    r = bisect_left(D, T-X)
    st.update(l, r, X)

for k in range(Q):
    ans = st.value(k)
    if ans == inf:
        ans = -1
    print(ans)
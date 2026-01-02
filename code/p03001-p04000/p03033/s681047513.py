import sys
input = sys.stdin.readline
from bisect import bisect_left

# 区間更新 1点取得
class SegmentTree:
    def __init__(self, N):
        tmp = 1
        while tmp < N:
            tmp <<= 1
        # self.N : 完全二分木の葉の数(N以上の最小の2べき)
        self.N = tmp
        # 2*self.N - 1 : 完全二分木のノード数
        # 1-indexedで管理するので1プラス
        self.data = [float('inf') for _ in range(2*self.N)]

    # [l, r)
    # 入力は0-indexedなので注意
    def update(self, l, r, x):
        L = l + self.N
        R = r + self.N
        while L < R:
            if L & 1:
                self.data[L] = min([self.data[L], x])
                L += 1
            if R & 1:
                R -= 1
                self.data[R] = min([self.data[R], x])
            L >>= 1
            R >>= 1

    def query(self, k):
        k += self.N
        res = self.data[k]
        while k != 1:
            k >>= 1
            res = min(res, self.data[k])
        return res



def main():
    N, Q = map(int, input().split())
    road = []
    for _ in range(N):
        S, T, X = map(int, input().split())
        road.append((S,T,X))

    D = [int(input()) for _ in range(Q)]

    st = SegmentTree(Q)
    for S, T, X in road:
        l = bisect_left(D, S - X)
        r = bisect_left(D, T - X)
        st.update(l, r, X)

    for q in range(Q):
        ans = st.query(q)
        if ans == float('inf'):
            print(-1)
        else:
            print(ans)

if __name__ == "__main__":
    main()
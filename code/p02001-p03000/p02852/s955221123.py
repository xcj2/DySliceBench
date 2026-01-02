import sys
input = sys.stdin.readline

inf = float('inf')

# 一点更新　区間取得　1-indexed
class SegmentTree:
    def __init__(self, n):
        tmp = 1
        while tmp < n:
            tmp <<= 1
        # self.N : 完全二分木の葉の数(N以上の最小の2べき)
        self.N = tmp
        # 2*self.N - 1 : 完全二分木のノード数
        # 1-indexedで管理するので１つ余分に設ける
        self.Data = [(inf, -1) for _ in range(2*self.N)]

    # k (0-indexed)
    def update(self, k, x):
        #　インデックスを補正
        k += self.N
        # 指定ノードを更新
        self.Data[k] = (x, k-self.N)
        # kを含む区間ノードを更新していく
        while k > 1:
            k >>= 1
            self.Data[k] = min([self.Data[2*k], self.Data[2*k+1]])

    # [l, r) (0-indexed)
    def query(self, l, r):
        #　インデックスを補正
        l += self.N
        r += self.N
        # 返り値を初期化
        res = (inf, -1)
        while l < r:
            # 右側なら右側を更新 右上に行く
            # 左側なら更新しない　上に行く
            if l & 1:
                res = min([res, self. Data[l]])
                l += 1
            # 右側なら左側を更新　上に行く
            # 左側なら更新しない 上に行く
            if r & 1:
                r -= 1
                res = min([res, self.Data[r]])
            l >>= 1; r >>= 1
        return res

    def value(self, k):
        k += self.N
        return self.Data[k]

N, M = map(int,input().split())
S = input()

ST = SegmentTree(N+1)
ST.update(0, 0)
memo = [-1] * (N+1)

for i in range(1, N+1):
    l = max(i-M, 0)
    r = i
    if S[i] == "0":
        d, j = ST.query(l, r)
        if d != inf:
            ST.update(i, d+1)
            memo[i] = j

if ST.value(N)[0] == inf:
    print(-1)
    exit()

ans = []
now = N
while now != 0:
    pre = memo[now]
    ans.append(now-pre)
    now = pre

print(*ans[::-1])
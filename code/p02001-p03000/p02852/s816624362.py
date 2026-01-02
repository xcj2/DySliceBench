N, M = map(int, input().split())
S = input()

# dp[i] := ゴールから最短何手でマスiにたどり着けるか
dp = [float('inf')] * (N + 1)
dp[-1] = 0


class RangeMinimumQuery:
    def __init__(self, n, inf=2 ** 31 - 1):
        self.n = 1 << (n - 1).bit_length()
        self.INF = inf
        self.segtree = [self.INF] * (2 * self.n)

    # i番目の値(0-indexed)をxに変更
    def update(self, i, x):
        i += self.n
        self.segtree[i] = x
        while i > 0:
            i //= 2
            self.segtree[i] = min(self.segtree[2 * i], self.segtree[2 * i + 1])

    # [l, r)のmin
    def query(self, l, r):
        L, R = l + self.n, r + self.n
        R = min(R, len(self.segtree))
        s = self.INF
        while L < R:
            if L & 1:
                s = min(s, self.segtree[L])
                L += 1

            if R & 1:
                s = min(s, self.segtree[R - 1])
                R -= 1

            L >>= 1
            R >>= 1

        return s


# セグメント木でdpテーブルを高速に埋める
RMQ = RangeMinimumQuery(N + 1)
RMQ.update(N, 0)
for i in range(N - 1, -1, -1):
    if S[i] == '1':
        continue

    # RMQ.query(l, r) := [l, r)の最小値
    dp[i] = RMQ.query(i, i + M + 1) + 1
    RMQ.update(i, dp[i])


ans = []
position = 0
while position < N:
    for move in range(1, M + 1):
        if position + move > N:
            continue

        if S[position + move] == '1':
            continue

        # 最短手数にならない
        if dp[position + move] == dp[position]:
            continue

        ans.append(move)
        position += move
        break

    else:
        print(-1)
        exit()

print(*ans)

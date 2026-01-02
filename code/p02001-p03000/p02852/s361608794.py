import sys
input = sys.stdin.readline

# 区間更新
# 小さいものを残すパターン
class RangeUpdateQuery:
    def __init__(self, n):
        self.n0 = 2**(n-1).bit_length()
        # 初期値
        self.INF = float("inf")
        self.data = [self.INF]*(2*self.n0-1)

    # 0-indexedで[l, r)をvに更新
    # [l, r]を更新したかったら (l, r+1)を引数に入れる
    # minが更新される場合だけ残す
    def update(self, l,r,v):
        l += self.n0
        r += self.n0
        while l < r:
            if r&1:
                r -= 1
                if self.data[r-1] > v:
                    self.data[r-1] = v
            if l&1:
                if self.data[l-1] > v:
                    self.data[l-1] = v
                l += 1
            l >>=1
            r >>=1

    def query(self, i):
        i += self.n0-1
        res = self.INF
        while i+1:
            if self.data[i] < res:
                res = self.data[i]
            i = ~-i//2
        return res

n,m = map(int, input().split())
s = input()[:-1]
DP = [-1]*(n+1)
seg = RangeUpdateQuery(n+1)
seg.update(0,1,0)

ss = s[::-1]
for i in range(n):
    if ss[i] == "1":
        continue
    cnt = seg.query(i)
    if cnt == float("inf"):
        continue
    seg.update(i+1, min(i+m+1, n+1), cnt+1)

if seg.query(n) == float("inf"):
    print(-1)
    exit()
a = [seg.query(i) for i in reversed(range(n+1))]
for i in range(n+1):
    if s[i] == "1":
        a[i] = float("inf")

prev = a[0]
j = 0
ans = []
for i in range(n+1):
    if a[i]<prev:
        prev = a[i]
        ans.append(i-j)
        j = i
print(*ans)
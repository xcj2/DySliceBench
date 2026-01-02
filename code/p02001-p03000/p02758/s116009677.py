from bisect import bisect_left

class SegTree:
    def __init__(self, raw_data):
        n = len(raw_data)
        self.size = 1 << (n.bit_length()) # 葉の要素数
        self.data = [0] * (2*self.size)
        self.build(raw_data)

    def build(self, raw_data):
        for i, x in enumerate(raw_data):
            self.data[self.size+i] = x
        for i in range(self.size-1, 0, -1):
            x = self.data[2*i]
            y = self.data[2*i+1]
            self.data[i] = x if x > y else y # ここを変更
    
    def update(self, i, x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            x = self.data[2*i]
            y = self.data[2*i+1]
            self.data[i] = x if x > y else y # ここを変更
            i >>= 1
    
    def get_data(self, i):
        return self.data[i+self.size]
    
    # これを変更
    def get_max(self, L, R):
        L += self.size
        R += self.size + 1
        x = 0
        while L < R:
            if L & 1:
                y = self.data[L]
                if x < y: x = y
                L += 1
            if R & 1:
                R -= 1
                y = self.data[R]
                if x < y: x = y
            L >>= 1
            R >>= 1
        return x

N = int(input())
robots = sorted([tuple(map(int, input().split())) for _ in range(N)])
X, D = zip(*robots)
mod = 998244353

affects = [0] + [bisect_left(X, x+d) for x, d in robots]
seg = SegTree(affects)

S = [0] * len(affects)
for n in range(N, 0, -1):
    affect = affects[n]
    x = seg.get_max(n, affect)
    S[n] = x
    seg.update(n, x)

dp = [0] * (N+1)
dp[0] = 1
dp_cum = [1] * (N+1)
for n, r in enumerate(S[1:], 1):
    dp[r] += dp_cum[n-1]
    dp[r] %= mod
    dp_cum[n] = dp_cum[n-1] + dp[n]
    dp_cum[n] %= mod
print(dp_cum[-1])


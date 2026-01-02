# AOJ DSL_2_A "Range Minimum Query"
# SegmantTreeの実装
import sys
input = sys.stdin.readline

# 初期化最大値
INF = 0

class SegmentTree:
    def __init__(self, N):
        self.N = 2**(N-1).bit_length()
        self.data = [-INF for _ in range(2*self.N-1)]
    
    # O(N)で初期化
    def compose(self, A):
        for k, a in enumerate(A):
            self.data[k+self.N-1] = a
        first = self.N - 1
        while first > 0:
            first = (first-1)//2
            for k in range(first, 2*first+1):
                if self.data[2*k+1] > self.data[2*k+2]:
                    self.data[k] = self.data[2*k+1]
                else:
                    self.data[k] = self.data[2*k+2]

    # k番目の値(0-indexed)をaに変更
    def update(self, k, a):
        self.data[k+self.N-1] = a
        k += self.N - 1
        while k > 0:
            k = (k-1)//2
            if self.data[2*k+1] > self.data[2*k+2]:
                self.data[k] = self.data[2*k+1]
            else:
                self.data[k] = self.data[2*k+2]

    # [l, r)
    # kがNodeの番号、対応する区間が[a, b)
    def query_max(self, l, r):
        if l+1 == r:
            return self.data[l+self.N-1]
        L = l + self.N
        R = r + self.N
        s = -INF
        while L < R:
            if R & 1:
                R -= 1
                if s < self.data[R-1]:
                    s = self.data[R-1]
            if L & 1:
                if s < self.data[L-1]:
                    s = self.data[L-1]
                L += 1
            L >>= 1; R >>= 1
        return s


def main():
    MAX = 3*10**5+5

    import sys
    input = sys.stdin.buffer.readline

    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ST = SegmentTree(MAX)
    # dp = [0]*(N+1)
    ans = 0
    for i, a in enumerate(A):
        maxscore = ST.query_max(max(a-K, 0), min(a+K+1, MAX))
        # dp[i+1] = dp[max(maxind, 0)] + 1
        ans = max(maxscore+1, ans)
        ST.update(a, maxscore+1)

    print(ans)

if __name__ == "__main__":
    main()
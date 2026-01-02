import sys
input = sys.stdin.readline
from bisect import bisect_left
inf = float('inf')

class SegmentTree:
    def __init__(self, N):
        tmp = 1
        while tmp < N:
            tmp <<= 1
        self.N = tmp
        self.data = [inf for _ in range(2*self.N-1)]
    
    def update(self, l, r, x):
        L = l + self.N - 1
        R = r + self.N - 1
        while L < R:
            if R & 1:
                R -= 1
                self.data[R] = min(self.data[R], x)
            if L & 1:
                self.data[L] = min(self.data[L], x)
                L += 1
            L >>= 1; R >>= 1
    
    def value(self, k):
        k += self.N - 1
        res = self.data[k]
        while k != 0:
            k >>= 1
            res = min(res, self.data[k])
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
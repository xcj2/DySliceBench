import sys
input = sys.stdin.readline
from bisect import bisect_left as bl
class segtree:
    def __init__(self, nn):
        self.NN = nn
        self.XX = [0] * (2**(nn+1)-1)
    def getmax(self, i):
        j = 2**self.NN + i - 1
        ma = -1
        while j >= 0:
            ma = max(ma, self.XX[j])
            j = (j-1) // 2
        return -1 if ma <= 0 else INF - ma
    def updaterange(self, a, b, x):
        l = a + (1<<self.NN)
        r = b + (1<<self.NN)
        s = 0
        while l < r:
            if l%2:
                self.XX[l-1] = max(self.XX[l-1], x)
                l += 1
            if r%2:
                r -= 1
                self.XX[r-1] = max(self.XX[r-1], x)
            l >>= 1
            r >>= 1

N, Q = map(int, input().split())
st = segtree(18)
INF = 1<<50
X = []
D = []
for _ in range(N):
    s, t, x = map(int, input().split())
    X.append((s, t, x))
for _ in range(Q):
    D.append(int(input()))

for s, t, x in X:
    st.updaterange(bl(D, s-x), bl(D, t-x), INF-x)
for i in range(Q):
    print(st.getmax(i))

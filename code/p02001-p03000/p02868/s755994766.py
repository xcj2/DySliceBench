# instead of AVLTree

INF = 10**14

class BIT():
    def __init__(self, max):
        self.max = max
        self.data = [INF]*(self.max+1)
    
    def update(self, i, x):
        while i > 0:
            self.data[i] = min(self.data[i], x)
            i -= i & -i

    def read(self, i):
        m = INF
        while i <= self.max:
            m = min(self.data[i], m)
            i += i & -i
        return m

import sys
input = sys.stdin.readline
from operator import itemgetter

N, M = map(int, input().split())
LRC = [list(map(int, input().split())) for _ in range(M)]
LRC.sort(key=itemgetter(0))

bit = BIT(N)
bit.update(1, 0)

for l, r, c in LRC:
    m = bit.read(l)
    bit.update(r, m+c)

ans = bit.data[N]
if ans == INF:
    print(-1)
else:
    print(ans)
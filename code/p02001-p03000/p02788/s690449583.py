from math import ceil
from bisect import bisect
from operator import itemgetter
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort(key=itemgetter(0))
X = [XH[i][0] for i in range(N)]
H = [XH[i][1] for i in range(N)]

bit = BIT(N)
ans = 0
for i in range(N):
    bit.add(i+1,H[i])
    bit.add(i+2,-H[i])
    h = bit.sum(i+1)
    if h>0:
        ans += ceil(h/A)
        x = -ceil(h/A)*A
        j = bisect(X,X[i]+2*D)
        bit.add(i+1,x)
        bit.add(j+1,-x)

print(ans)

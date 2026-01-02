from operator import itemgetter
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
xy.sort(key=itemgetter(1))
for i in range(N):
    xy[i][1] = i
xy.sort(key=itemgetter(0))

mod = 998244353
p2 = [1]*(N+1)
for i in range(N):
    p2[i+1] = p2[i]*2%mod

bit = BIT(N)

ans = 0

for i in range(N):
    y = xy[i][1]
    bit.add(y,1)
    n1 = i+1-bit.sum(y)
    n2 = i-n1
    n3 = N-y-1-n1
    n4 = N-i-1-n3
    ans += 1
    ans += (p2[n1]-1)+(p2[n2]-1)+(p2[n3]-1)+(p2[n4]-1)
    ans += (p2[n1]-1)*(p2[n2]-1)+(p2[n3]-1)*(p2[n4]-1)+(p2[n1]-1)*(p2[n3]-1)+(p2[n2]-1)*(p2[n4]-1)+2*(p2[n1]-1)*(p2[n4]-1)+2*(p2[n2]-1)*(p2[n3]-1)
    ans += 2*((p2[n1]-1)*(p2[n2]-1)*(p2[n3]-1)+(p2[n1]-1)*(p2[n2]-1)*(p2[n4]-1)+(p2[n1]-1)*(p2[n3]-1)*(p2[n4]-1)+(p2[n2]-1)*(p2[n3]-1)*(p2[n4]-1))
    ans += 2*(p2[n1]-1)*(p2[n2]-1)*(p2[n3]-1)*(p2[n4]-1)
    ans %= mod
print(ans)
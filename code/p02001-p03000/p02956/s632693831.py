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

mod = 998244353

N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
xy.sort(key=itemgetter(1))
for i in range(N):
    xy[i][1] = i+1
xy.sort(key=itemgetter(0))

pow2 = [1]*(N+1)
for i in range(N):
    pow2[i+1] = 2*pow2[i]%mod

ans = pow2[N-1]*N%mod

bit = BIT(N)
for i in range(N):
    l1 = bit.sum(xy[i][1])
    l2 = i-l1
    r1 = xy[i][1]-l1-1
    r2 = N-xy[i][1]-l2
    bit.add(xy[i][1],1)
    ans += (pow2[l2]-1)*(pow2[r1]-1)*pow2[r2]*pow2[l1]
    ans += (pow2[r2]-1)*(pow2[l1]-1)*(pow2[l2]+pow2[r1]-1)
    ans %= mod

print(ans)
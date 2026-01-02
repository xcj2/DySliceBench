N, M = map(int, input().split())
mod = 10**9+7
# コンビネーションクラスの作成


class Data():
    def __init__(self):
        self.power = 1
        self.rev = 1


class Combi():
    def __init__(self, N, mod):
        self.lists = [Data() for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.lists[i].power = ((self.lists[i-1].power)*i) % self.mod
        self.lists[N].rev = pow(self.lists[N].power, self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.lists[j-1].rev = ((self.lists[j].rev)*j) % self.mod

    def combi(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.lists[K].power)*(self.lists[K-R].rev)*(self.lists[R].rev)) % self.mod


c = Combi(10**6, mod)
ans = (c.lists[M].power*c.lists[M-N].rev)**2 % mod
for k in range(1, N+1):
    s = (-1)**((k-1) % 2)
    t = c.combi(N, k)
    u=((c.lists[M-k].power*c.lists[M-N].rev)**2) % mod
    v=(c.lists[M].power*c.lists[M-k].rev) % mod
    ans -= s*t*u*v
print(ans % mod)
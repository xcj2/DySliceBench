class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(self.power_func(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(self.power_func(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __row__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )

    def power_func(self,a,n,p):
        bi=str(format(n,"b"))#2進表現に
        res=1
        for i in range(len(bi)):
            res=(res*res) %p
            if bi[i]=="1":
                res=(res*a) %p
        return res

    def combination(self,n,r=-1):
        if r==-1:
            r = n
        #nCrの一覧を返す。rの上限も
        if (r<0) or (n<r):
            return 0
        cur = ModInt(1)
        res = []
        res.append(cur)
        for i in range(1,r+1):
            cur *= n + 1 -i
            cur /= i
            res.append(cur)
        return res

MOD = 998244353
#グローバル変数MODを決めてあげてください
#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

N,S = [int(hoge) for hoge in input().split()]
A = [int(hoge) for hoge in input().split()]

DP = [[0]*(S+1) for i in range(N+1)]#DP[k][x] = i個みて和がx 
DP[0][0] = 1
Modi2 = mod_inv(2,MOD)
for i in range(N):
    a = A[i]
    #くばるDP
    for s,d in enumerate(DP[i]):
        DP[i+1][s] += DP[i][s]
        DP[i+1][s] %= MOD
        Diff = d*Modi2
        Diff %= MOD
        if s + a  <= S:
            DP[i+1][s+a] += Diff
            DP[i+1][s+a] %= MOD

two = ModInt(2)
twotwo = two ** ModInt(N)
print(DP[N][S] * twotwo)

    
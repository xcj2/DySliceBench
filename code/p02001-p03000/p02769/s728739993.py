MOD=10**9+7
n,k=map(int,input().split())
def modpow(a, p, mod=MOD):
    # return a**p (mod MOD) O(log p)
    if p==0: return 1
    if p%2==0:
        half = modpow(a, p//2, mod)
        return half*half % mod
    else:
        return a * modpow(a, p-1, mod) % mod

ret=modpow(2,n)
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
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
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

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )
def comb(x,n):
    divd=1
    for i in range(n):
        divd*=ModInt(x-i)
    for i in range(n):
        divd/=ModInt(i+1)
    return divd
if k<n-1:
    combl_1=[1]*n
    combl_2=[1]*(n+1)
    combl_1[1]=n-1
    combl_2[1]=n
    for i in range(2,n):
        combl_1[i]=ModInt(n-i)*combl_1[i-1]/ModInt(i)
        combl_2[i]=ModInt(n-i+1)*combl_2[i-1]/ModInt(i)
    ans=0
    for i in range(k+1):
        ans+=combl_1[i]*combl_2[i]
    print(ans)
if k>=n-1:
    print(comb(2*n-1,n-1))
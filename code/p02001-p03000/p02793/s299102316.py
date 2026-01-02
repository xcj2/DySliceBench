N=int(input())
*A,=map(int, input().split())
M=10**3

P=[]
isp=[True]*M
for n in range(2,M):
    if isp[n]==False: continue
    P.append(n)
    for m in range(n*n, M, n):
        isp[m]=False

from collections import defaultdict
D=[defaultdict(int) for _ in range(N)]
for i in range(N):
    a=A[i]
    for p in P:
        while a>1:
            if a%p==0:
                D[i][p]+=1
                a//=p
            else:
                break
        else:
            break
    if a>1:
        D[i][a]+=1

d=defaultdict(int)
for i in range(N):
    for k,v in D[i].items():
        d[k] = max(d[k], v)

MOD = 10**9+7
class Mint:
    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value += Mint.get_value(other)
        if self.value >= MOD: self.value -= MOD
        return self
    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value -= Mint.get_value(other)
        if self.value < 0: self.value += MOD
        return self
    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj
    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self
    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self
    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj
    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj

gcd=Mint(1)
for k,v in d.items():
    gcd *= pow(k,v,MOD)

print(sum([gcd//a for a in A]))

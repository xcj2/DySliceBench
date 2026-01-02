import math
from collections import Counter
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



#グローバル変数MODを決めてあげてください
MOD = 1000000007

N = int(input())
#双方ノンゼロ...
#Ai*Aj = - Bi* Bj　⇔　Ai/Bi == -Bj/Ai
#絶対値が同じやつら
#片方ゼロ→ノンゼロとは食い合わないがもう片方がゼロならダメ
#両方ゼロ→単騎で選ぶしかない
#ノンゼロ組、片方ゼロ組、両方ゼロ組に分ける
#ノンゼロ*(1 + Aだけゼロ + Bだけゼロ) + 両方ゼロ単騎
#1,1組→ 
NonZeroPlus = []
NonZeroMinus = []
a = ModInt(2)
AZero = 0
BZero = 0
TwoZero = 0
TwoOne = 0
for n in range(N):
    A,B = [int(hoge) for hoge in input().split()]
    if A!=0 and B!=0:
        G = math.gcd(abs(A),abs(B))
        if B < 0:
            G *= -1
            #B//Gが必ず正
        if A//G > 0:
            NonZeroPlus.append((A//G,B//G))
        else:#A//B < 0
            NonZeroMinus.append((B//G,-A//G))
    elif A==B==0:
        TwoZero += 1
    elif A == 0:
        AZero += 1
    else:
        BZero += 1
P = Counter(NonZeroPlus)
M = Counter(NonZeroMinus)
NonZero = ModInt(1)
Daburazu = ModInt(0)
for k in P.keys():
    X,Y = P[k],M[k]
    if Y:
        NonZero *= (a**X -1) + (a**Y -1) + 1 
    else:
        Daburazu += X
for k in M.keys():
    X,Y = P[k],M[k]
    if X == 0:
        Daburazu += Y
#ノンゼロ組…コレ(0含む)
NonZero *= a**Daburazu
NonZero *= (a**AZero -1) + (a**BZero -1) + 1
NonZero += TwoZero
print(NonZero -1)
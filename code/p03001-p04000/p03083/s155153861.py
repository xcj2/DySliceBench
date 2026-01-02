b,w=map(int,input().split())
MOD=10**9+7
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
factorial=[ModInt(1)]*(b+w+1)
for i in range(1,b+w+1):
    factorial[i]=factorial[i-1]*i
power_of_two=ModInt(1)
def comb(count, BorW):
    if count < BorW:return 0
    return factorial[count]/factorial[BorW]/factorial[count-BorW]
Black_doesnt_exist=[0]*(w+1)
White_doesnt_exist=[0]*(b+1)
Black_doesnt_exist[0]=ModInt(1)
White_doesnt_exist[0]=ModInt(1)
for i in range(b):
    Black_doesnt_exist[0]*=2
for i in range(w):
    White_doesnt_exist[0]*=2
Black_doesnt_exist[0]-=1;White_doesnt_exist[0]-=1
#Blackdoesn'texist[i]:=b+i個から0~b-1個を選ぶ選び方の総数
for i in range(1,w+1):
    Black_doesnt_exist[i]=Black_doesnt_exist[i-1]*2-comb(b+i-1,b-1)
for i in range(1,b+1):
    White_doesnt_exist[i]=White_doesnt_exist[i-1]*2-comb(w+i-1,w-1)
for i in range(b+w):
    B=0;W=0
    #B:前回までに黒いチョコを食べきっているような選び方
    #W:前回までに白いチョコを食べきっているような選び方
    if i>=b:
        B=power_of_two-Black_doesnt_exist[i-b]
    if i>=w:
        W=power_of_two-White_doesnt_exist[i-w]
    Both_exist=power_of_two-B-W
    print(W/power_of_two+Both_exist/power_of_two/2)
    power_of_two*=2
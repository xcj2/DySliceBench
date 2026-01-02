MOD = 10**9 + 7
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
    


def main():
    from sys import stdin
    input = stdin.readline
    from operator import mul
    from functools import reduce
    import math
    fact = math.factorial

    def cmb(n,r):
        n = int(str(n))
        r = int(str(r))
        r = min(n-r,r)
        if r == 0: return 1
        u = [1]
        l = [1]
        #print(n,n-r)
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1,r + 1))
        return over // under

    

    def hoge(n,r):
        num = 1
        for i in range(int(str(n)),   int(str(n-r))  ,-1):
            num *= i
        for i in range(1,int(str(r))+1):
            num //= i
        return num

    
    N,K= map(int, input().split())
    red = N-K
    blue = K
    
    print(N-K+1)
    for i in range(2,K+1):
        #print(ModInt(cmb(K-1,i-1))  ,         fact(red+1)//fact(i)//fact(red+1-i))
        print(    hoge(red+1,i)  * ModInt(cmb(K-1,i-1))       )

if __name__ == '__main__':
    main()
def main():
    import sys
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    MOD = 998244353
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

    n,k = ina()
    dp = [ModInt(0)]*(n+1)
    dp[1] = 1
    pair = [(0,0)]*k
    for i in range(k):
        l,r = ina()
        pair[i] = (l,r)
    for i in range(1,n):
        tmp = i
        dp[tmp]+=dp[tmp-1]
        for j in range(k):
            if(tmp+pair[j][0])<=n:
                # print(tmp,pair[j][0])
                dp[tmp+pair[j][0]]+=dp[tmp]
                # print(dp)
            if(tmp+pair[j][1])<=n-1:
                # print(tmp,pair[j][1])
                dp[tmp+pair[j][1]+1]-=dp[tmp]
                # print(dp)
    # print(dp)
    print(dp[n])
        
        
    

    
    
        


    
        


        


    




















if __name__ == "__main__":
    main()
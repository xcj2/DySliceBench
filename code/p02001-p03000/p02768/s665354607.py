class Mint:
    
    MOD = 10**9+7
    
    def __init__(self, x=0):
        self.x = (x%self.MOD + self.MOD) % self.MOD
    
    def __iadd__(self, other):
        self.x += other.x
        if self.x >= self.MOD:
            self.x -= self.MOD
        return self
    
    def __isub__(self, other):
        self.x += self.MOD - other.x
        if (self.x >= self.MOD):
            self.x -= self.MOD
        return self
    
    def __imul__(self, other):
        self.x *= other.x
        self.x %= self.MOD;
        return self;
    
    def __add__(self, other):
        ans = Mint(self.x)
        ans += other
        return ans
        
    def __sub__(self, other):
        ans = Mint(self.x)
        ans -= other
        return ans
    
    def __mul__(self, other):
        ans = Mint(self.x)
        ans *= other
        return ans
    
    def __pow__(self, n):
        if n == 0:
            return Mint(1)
        a = self.__pow__(n >> 1)
        a *= a
        if n&1:
            a *= self
        return a
    
    def inv(self):
        return self**(self.MOD-2)
    
    def __ifloordiv__(self, other):
        self *= other.inv()
        return self
    
    def __floordiv__(self, other):
        ans = Mint(self.x)
        ans //= other
        return ans
        
class Comb:
    
    def __init__(self):
        pass
    
    def comb(self, n, k):
        assert n < Mint.MOD
        if k < 0 or k > n:
            return 0
        numerator = Mint(n-k+1)
        for i in range(n-k+2, n+1):
            numerator *= Mint(i)
        d = Mint(1)
        for i in range(2, k+1):
            d *= Mint(i)
        denominator = d.inv()
        return numerator*denominator            
        

def Main(N, A, B):
    ans = Mint(2)**N-Mint(1)-Comb().comb(N, A)-Comb().comb(N, B)
    return ans.x

def main():
    N, A, B = list(map(int, input().split()))
    print(Main(N, A, B))

if __name__ == '__main__':
    main()
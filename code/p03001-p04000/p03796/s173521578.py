N = int(input())

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
        
        
def Main(N):
    ans = Mint(1)
    for i in range(1, N+1):
        ans *= Mint(i)
    return ans.x
    
print(Main(N))
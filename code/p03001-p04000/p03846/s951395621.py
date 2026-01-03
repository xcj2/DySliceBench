N = int(input())
A = list(map(int, input().split()))

from collections import Counter

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
        
    

def Main(N, A):
    counter = Counter(A)
    if len(A)%2 == 0:
        v = counter.values()
        s = set(v)
        if len(s) > 1:
            return 0
        else:
            k = list(counter.keys())
            k.sort()
            for i, e in enumerate(k):
                if e != 2*i+1:
                    return 0
            return (Mint(2)**(len(A)//2)).x
    else:
        if 0 not in counter:
            return 0
        if 0 in counter and counter[0] != 1:
            return 0
        del counter[0]
        v = counter.values()
        s = set(v)
        if len(s) > 1:
            return 0
        else:
            k = list(counter.keys())
            k.sort()
            for i, e in enumerate(k):
                if e != 2*(i+1):
                    return 0
            return (Mint(2)**(len(A)//2)).x           
                    
                

res = Main(N, A)
print(res)
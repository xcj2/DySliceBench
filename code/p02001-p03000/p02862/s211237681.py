class Combination:
    def __init__(self, mod, max_n):
        self.MOD = mod
        self.MAX_N = max_n

        self.f = self.factorial(self.MAX_N)
        self.f_inv = [self.inv(x) for x in self.f]

    def inv(self,x):
        return pow(x, self.MOD-2, self.MOD)
    
    def factorial(self, n):
        res = [1]
        for i in range(1,n+1):
            res.append(res[-1] * i % self.MOD)
        return res
    
    def comb(self, n, r):
        return (self.f[n] * self.f_inv[r] % self.MOD) * self.f_inv[n-r] % self.MOD


X, Y = map(int,input().split())
k, l = (2*Y-X)//3, (2*X-Y)//3

if (X + Y) % 3 != 0 or k < 0 or l < 0:
    print(0)
    exit()

CB = Combination(10**9+7, k+l)
print(CB.comb(k+l,k))
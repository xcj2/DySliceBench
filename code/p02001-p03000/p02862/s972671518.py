class Factorials(object):
    def __init__(self, n, mod):
        inv = [1] * (n + 1)
        self.__mod = mod
        self.__fac = [1] * (n + 1)
        self.__fac_inv = [1] * (n + 1)
        for i in range(2, n+1):
            self.__fac[i] = (self.__fac[i-1] * i) % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            self.__fac_inv[i] = self.__fac_inv[i - 1] * inv[i] % mod
        
    def comb(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        return self.__fac[n] * (self.__fac_inv[k] * self.__fac_inv[n - k] % self.__mod) % self.__mod
    
    def fac(self, k):
        return self.__fac[k]
    
    def fac_inv(self, k):
        return self.__fac_inv[k]

MOD = 1000000007
x, y = map(int, input().split())
if (x + y) % 3 != 0:
  print(0)
  exit()
n = (x + y) // 3
f = Factorials(n, MOD)
print(f.comb(n, x-n))
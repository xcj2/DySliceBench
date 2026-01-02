import sys
input = sys.stdin.readline


class Comb:
    def __init__(self, n, mod=pow(10, 9)+7, f=True, i=False, version=False):
        self.n = n
        self.mod = mod
        self.mod_inv = mod-2 if version else -1
        self.factorial_table = None
        self.inverse_table = None
        if f: self.get_factorial()
        if i: self.get_inverse()
        
    def get_factorial(self):
        self.factorial_table = [1]*(self.n+1)
        for i in range(1, self.n+1):
            self.factorial_table[i] = self.factorial_table[i-1]*i%self.mod
        self.inverse_table = None
    
    def get_inverse(self):
        mod = self.mod
        mod_inv = self.mod_inv
        self.inverse_table = [1]*(self.n+1)
        for i in range(self.n+1):
            self.inverse_table[i] = pow(self.factorial_table[i], mod_inv, mod)
    
    def factorial(self, n):
        if self.factorial_table == None:
            return None
        return self.factorial_table[n]
    
    def inverse(self, n):
        if self.inverse_table == None:
            return None
        return self.inverse_table[n]   
    
    def permutation(self, n, k):
        if self.factorial_table == None:
            return None
        mod = self.mod
        mod_inv = self.mod_inv
        if self.inverse_table == None:
            return self.factorial_table[n]*pow(self.factorial_table[n-k], mod_inv, mod)%mod
        return self.factorial_table[n]*self.inverse_table[n-k]%mod
            
    def comb(self, n, k):
        if self.factorial_table == None:
            return None
        mod = self.mod
        mod_inv = self.mod_inv
        if self.inverse_table == None:
            res = self.factorial_table[n]*pow(self.factorial_table[n-k], mod_inv, mod)%mod\
                                    *pow(self.factorial_table[k], mod_inv, mod)%mod
        else:
            res = self.factorial_table[n]*self.inverse_table[n-k]%mod\
                                    *self.inverse_table[k]%mod
        return res
    
    def recomb(self, n, k):
        if n+k-1 > self.n:
            return None
        return self.comb(n+k-1, k)


def main():
    r1, c1, r2, c2 = map(int, input().split())
    comb = Comb(10**6*2+1, version=True)
    mod = pow(10, 9) + 7

    ans = 0
    comb1, comb2 = comb.comb(c1+r2+1, r2+1), comb.comb(c1+r1, r1)
    for key in range(c1, c2+1):
        sub = (((r2+1) * comb1 - r1 * comb2) * pow(key+1, mod-2, mod)) % mod
        ans = (ans + sub) % mod

        comb1 = comb1 * (key + r2 + 2) * pow(key+1, mod-2, mod) % mod
        comb2 = comb2 * (key + r1 + 1) * pow(key+1, mod-2, mod) % mod


    print(ans)


    
if __name__ == "__main__":
    main()



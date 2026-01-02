
import numpy as np

MOD = 1000000007


class Combination:
    def __init__(self, n):
        self.n = n
        self.fac, self.facinv = self.make_fact(n, MOD)

    def cumprod(self, arr,MOD):
        L = len(arr); Lsq = int(L**.5+1)
        arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
        for n in range(1,Lsq):
            arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
        for n in range(1,Lsq):
            arr[n] *= arr[n-1,-1]; arr[n] %= MOD
        return arr.ravel()[:L]
    
    def make_fact(self, U,MOD):
        x = np.arange(U,dtype=np.int64); x[0] = 1
        fact = self.cumprod(x,MOD)
        x = np.arange(U,0,-1,dtype=np.int64); x[0] = pow(int(fact[-1]),MOD-2,MOD)
        fact_inv = self.cumprod(x,MOD)[::-1]
        return fact,fact_inv


    def nck(self, n, k):
        if k == 0 or n == k:
            return 1
        return self.fac[n] * self.facinv[k] % MOD * self.facinv[n-k] % MOD;

    def get(n):
        return self.fac[n]
    
    def getinv(n):
        return self.facinv[n]

if __name__ == "__main__":
    X,Y = map(int, input().split())
    cb = Combination(1000010)
    if (X+Y) % 3 != 0:
        print(0)
        exit(0)
    if X > Y:
        if X > 2*Y:
            print(0)
            exit(0)
    else:
        if Y > 2*X:
            print(0)
            exit(0)
    a = (2 * Y - X) // 3
    b = (2 * X - Y) // 3
    print(cb.nck(a+b, a))

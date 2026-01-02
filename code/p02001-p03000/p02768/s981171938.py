import sys
input = sys.stdin.buffer.readline
import math
import copy

def main():
    N,a,b = map(int,input().split())
    MOD = 10**9+7

    fac = [0 for _ in range(2*10**5+1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,2*10**5+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD
        
    def coef(x,y):
        num = (((fac[x]*invfac[y])%MOD)*invfac[x-y]%MOD)
        return num

    def nume(N, r, mod):
        x = 1
        for i in range(1, r + 1):
            x = x * (N-i+1) % mod 
        return x

    s = pow(2,N,MOD) 
    a = nume(N,a,MOD)*invfac[a]
    b = nume(N,b,MOD)*invfac[b]
    ans = (s-1-a-b) % MOD

    print(int(ans))
    
if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    N,K = map(int,input().split())
     
    def modpow(a,n,mod):
        res = 1
        while n > 0:
            if n & 1:
                res = res * a % mod
            a = a * a % mod
            n >>= 1
        return res
     
    def modinv(a,mod):
        return modpow(a,mod - 2,mod)
     
    def cnk(a,b):
        MOD = 10**9+7
        ret = 1
        for i in range(b):
            ret *= (a-i)
            ret %= MOD
            ret = ret * modinv(i+1,MOD) % MOD
        return ret
     
     
    for i in range(1,K+1):
        if i > N - K +1:
            print(0)
        elif i == 1:
            print(N-K+1)
        else:
            print(cnk(N-K+1,i)*cnk(K-1,i-1)%(10**9+7))
if __name__ == '__main__':
    main()

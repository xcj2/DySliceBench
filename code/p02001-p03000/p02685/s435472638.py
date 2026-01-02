import sys
sys.setrecursionlimit(10**9)

def main():
    N,M,K = map(int,input().split())
    MOD = 998244353

    def get_fact(maxim,mod):
        maxim += 1
        fact = [0]*maxim

        fact[0] = 1
        for i in range(1,maxim):
            fact[i] = fact[i-1] * i % mod

        invfact = [0]*maxim
        invfact[maxim-1] =  pow(fact[maxim-1],mod-2,mod)

        for i in reversed(range(maxim-1)):
            invfact[i] = invfact[i+1] * (i+1) % mod

        return fact, invfact

    def powerful_comb(n,r,mod,fact,invfact):
        return fact[n] * invfact[r] * invfact[n-r] % mod

    ans = 0
    fact, invfact = get_fact(N+1,MOD)
    for i in range(K+1):
        ans += (M*pow(M-1,N-i-1,MOD) * powerful_comb(N-1,i,MOD,fact,invfact)) % MOD

    print(ans % MOD)

if __name__ == "__main__":
  main()
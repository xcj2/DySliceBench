import sys
sys.setrecursionlimit(10**9)

def main():
    N,K = map(int,input().split())
    A = [0] + sorted(list(map(int,input().split())))
    MOD = 10**9+7

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
        if n < 0 or n < r: return 0
        return fact[n] * invfact[r] * invfact[n-r] % mod

    ans = 0
    fact,invfact = get_fact(N,MOD)
    for i in range(K,N+1):
        ans += ((A[i]-A[N-i+1]) * powerful_comb(i-1,K-1,MOD,fact,invfact)) % MOD

    print(ans % MOD)
    # print(A)

if __name__ == "__main__":
  main()
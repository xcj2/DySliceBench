import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N,M,K=MI()
    
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
        
        
    p=[1]*(N+3)#(M-1)^i
    for i in range(N+2):
        p[i+1]=(p[i]*(M-1))%mod
        
    ans=0
    for i in range(K+1):
        temp=M*p[N-1-i]*cmb(N-1,i,mod)
        temp%=mod
        ans=(ans+temp)%mod
        
    print(ans)

main()

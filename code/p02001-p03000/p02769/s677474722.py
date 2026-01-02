import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


def main():
    mod=10**9+7
    N,K=MI()
    
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]

    for i in range(2, N*2 + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)

    ans=0
    
    #空き部屋がk個
    for i in range(min(K+1,N)):
        a=i#動く人
        b=N-i#割り当てる部屋
        temp=cmb(a+b-1,a,mod)
        
        #空き部屋の選び方
        temp2=cmb(N,i,mod)
        temp*=temp2
        
        ans=(ans+temp)%mod
        
    print(ans)
        
    

main()

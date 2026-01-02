

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    K=I()
    S=input()
    N=len(S)
    
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, N+K+2 + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    
    #Sの条件を初めて満たした時の末端いちで場合分け
    
    #i文字目が末端で，自由枠がj個（iが決まればjも決まるけど，まとめやすいので）
    def calc(i,j):
        temp=pow(26,K-j,mod)#残りの完全自由枠
        temp=(temp*pow(25,j,mod)*cmb(i-1,j,mod))%mod
        return temp
    
    ans=0
    for j in range(K+1):
        i=j+N
        ans=(ans+calc(i,j))%mod
        
    print(ans)


main()

import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=I()
    
    N=10000
    
    #0~Nまで逆元などを事前計算

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
        
    ans=0
    
    for i in range(1,N):#i此のグル-ぷに分ける
        if 3*i > S:
            break
        s2=S-i*3
        temp=cmb(s2+i-1,i-1,mod)
        ans=(ans+temp)%mod
        
    print(ans)
        
        
    

main()

import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    
    ###################################
    #0~Nまで逆元などを事前計算
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, max(N,M) + 3):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    ###################################
    
    """
    Aは固定．
    
    「1つもない」は数え辛い，「少なくともk個ある」は数えやすい
    i=Piがk個以上ある
        kこ選ぶ：NCK
        残りを適当に並べる：(M-K)PK
        係数：(-1)^k
    
    """
    ans=0
    for k in range(N+1):
        cm=cmb(N,k,mod)
        rem=(fact[M-k]*factinv[M-N])%mod
        if k%2==0:
            c=1
        else:
            c=-1
        ans=(ans+c*cm*rem)%mod
        
    ans=(ans*fact[M]*factinv[M-N])%mod
    print(ans)
    
    


        
    

main()

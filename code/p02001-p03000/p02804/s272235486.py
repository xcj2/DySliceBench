import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    A.sort()
    
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
        
    
    def calc(ii,a):
        # ii番目が最大となる時，それの寄与は？
        # 0~ii-1のii個からK-1個えらぶ
        temp=cmb(ii,K-1,mod)
        return (temp*a)%mod
    
    ans=0
    for i in range(N):
        ans+=calc(i,A[i])
        
    for i in range(N):
        A[i]*=-1
    A.sort()
    for i in range(N):
        ans+=calc(i,A[i])
        
    print(ans%mod)
        
    
    
    

main()

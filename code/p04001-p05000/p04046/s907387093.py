import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,A,B=MI()

    
    N=H+W
    
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
        
        
    ans=cmb(N-2,H-1,mod)
    
    for i in range(min(A,B)):
        h=H-A+i+1
        w=B-i
        #print(h,w,cmb(h+w-2,h-1,mod),cmb(H+W-(h+w),H-h,mod))
        ans-=cmb(h+w-2,h-1,mod)*cmb(H+W-(h+w),H-h,mod)
        ans%=mod
        
    print(ans%mod)

main()

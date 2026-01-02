NUM = 10**5 + 1
MOD = 10**9 + 7
dp = [-1] * NUM
dp[0] = 1
for i in range(1, NUM):
    dp[i] = (dp[i-1] * i) % MOD

def inv(p): 
    res = 1 
    k = MOD - 2 
    while k > 0:
        if k & 1:
            res = (res * p) % MOD 
        p = (p * p) % MOD 
        k //= 2
    return res
            
def comb(n, k): 
    p = dp[n]
    q = (dp[n-k] * dp[k]) % MOD
    return (p * inv(q)) % MOD
                    
def solve(n, k, a):         
    a = sorted(a)                   
    minX = sum(comb(n-l, k-1) * a[l-1] for l in range(1,n+1) if l+k-1 <= n)
    maxX = sum(comb(r-1, k-1) * a[r-1] for r in range(1,n+1) if r >= k)
    return (maxX - minX) % MOD                                          
                                                                                    
n, k = map(int, input().split())                                                                
a = list(map(int, input().split()))                                                                     
print(solve(n, k, a))  
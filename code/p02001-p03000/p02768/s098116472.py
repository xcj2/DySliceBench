N,a,b = [int(i) for i in input().split()]
mod = 10**9+7
def power(x, n):
    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = ans*x%mod
        x = (x*x)%mod
        n = n >> 1 #ビットシフト
    return ans
def fact(m, n):
    val = 1
    for i in range(m, n+1):
        val = val*i % mod
    return val
    
def cmb1(N, r):
    A = fact(N-r+1, N)%mod
    B = fact(1, r)%mod
    return A, B, (A*power(B, mod-2))%mod
def cmb2(a, b, A, B):
    A = fact(N-a+1, N-b)*A%mod
    B = fact(b+1, a)*B%mod
    return (A*power(B, mod-2))%mod
if(a>N//2):
    a = N-a
if(b>N//2):
    b = N-b
tmp = max(a,b)
b = min(a,b)
a = tmp
A, B, K1 = cmb1(N, b)
K2 = cmb2(a, b, A, B)
print((power(2, N)-1-K1-K2)%mod)
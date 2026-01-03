H,W,A,B = map(int, input().split())
N = H+W

MOD = 10**9 + 7

def mul(a, b):
    return ((a % MOD) * (b % MOD)) % MOD
  
def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % MOD
    elif y % 2 == 0 : return power(x, y//2)**2 % MOD
    else            : return power(x, y//2)**2 * x % MOD

def div(a, b):
    return mul(a, power(b, MOD-2))

# 階乗計算
fac = [1] * N
for i in range(1, N): 
    fac[i] = fac[i-1] * i % MOD
    
invfac = [0] * (N)
invfac[H+W-1] = power(fac[H+W-1], MOD-2)
for i in range(H+W-2, -1, -1):
    invfac[i] = invfac[i+1] * (i+1) % MOD
    
def nCr(n, r):
    return fac[n] * invfac[r] * invfac[n-r] % MOD



ans = 0
f = {}
for i in range(H-A):
    h1 = i
    w1 = B-1
    if (h1, w1) in f:
        zenhan = f[(h1, w1)]
    else:
        zenhan = nCr(h1+w1,h1)
        f[(h1, w1)] = zenhan
    
    h2 = (H-1) - i
    w2 = (W-1) - B
    if (h2, w2) in f:
        kouhan = f[(h2, w2)]
    else:
        kouhan = nCr(h2+w2,h2)
        f[(h2, w2)] = kouhan

    ans += zenhan * kouhan

print(ans % MOD)
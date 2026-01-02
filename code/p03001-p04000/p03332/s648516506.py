N,A,B,K = map(int,input().split())
if A<B: A,B = B,A
MOD = 998244353

def mul(a,b):
    return (a*b) % MOD

def pow(a,n): # a^n
    ret = 1
    mag = a
    while n > 0:
        if n & 1:
            ret = mul(ret, mag)
        mag = mul(mag, mag)
        n >>= 1
    return ret

def inv(a):
    return pow(a, MOD-2)

fac = [1]
fac_inv = [1]
for n in range (1,N+10):
    f = mul(fac[n-1], n)
    fac.append(f)
    fac_inv.append(inv(f))

mem = [0] * (N+1)
def ncr(n,r):
    if mem[r] > 0:
        return mem[r]
    else:
        ret = mul(mul(fac[n], fac_inv[n-r]), fac_inv[r])
        mem[r] = ret
        return ret

ans = 0
for a in range(N+1):
    if a*A > K: break
    rem = K-a*A
    if rem%B: continue
    b = rem//B
    if b > N: continue
    ans += mul(ncr(N,a), ncr(N,b))
print(ans % MOD)

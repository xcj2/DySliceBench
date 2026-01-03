# nの逆元のリスト
def inv_mod(n:int, mod:int) -> list:
    inv = [0,1]
    for i in range(2,n+1):
        inv.append(mod - ((mod//i)*inv[mod%i]) % mod)
    return inv
       
# nの階乗のリスト
def fact(n:int, mod:int) -> list:
    fac = [1,1]
    res = 1
    for i in range(2,n+1):
        res = res*i%mod
        fac.append(res)
    return fac

# nの階乗の逆元のリスト
def fact_inv(n:int, inv:list, mod:int) -> list:
    facInv = [1,1]
    for i in range(2,n+1):
        facInv.append(facInv[i-1]*inv[i] % mod)
    return facInv
        
# 二項係数
def nCr(n:int, r:int, mod:int, fac:list, facInv:list) -> int:
    if n==0 and r==0:
        return 1

    elif not (0<=r and r<=n):
        return 0
    
    return ((fac[n]*facInv[r]) % mod) * facInv[n-r] % mod


H,W,A,B = map(int, input().split())
mod = 10**9+7

inv = inv_mod(H+W, mod)
fac = fact(H+W, mod)
facInv = fact_inv(H+W,inv,mod)

checkPoint = []
for i in range(H-A):
    checkPoint.append((i,B-1))
    
ans = 0
for h,w in checkPoint:
    ans = (ans + nCr(h+w,h,mod,fac,facInv) \
                * nCr(H+W-h-w-3, H-h-1, mod, fac, facInv)) % mod
    
print(ans)
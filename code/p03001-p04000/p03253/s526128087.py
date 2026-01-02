def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fac[n]*finv[r]*finv[n-r]%p

def perm(n,r,p):
  if (r < 0) or (n < r):
    return 0
  return fac[n]*finv[n-r]%p

n = 2*pow(10,5)+10
MOD = pow(10,9)+7

fac = [-1]*(n+1); fac[0] = 1; fac[1] = 1 #階乗
finv = [-1]*(n+1); finv[0] = 1; finv[1] = 1 #階乗の逆元
inv = [-1]*(n+1); inv[0] = 0; inv[1] = 1 #逆元
for i in range(2,n+1):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
 
    if temp!=1: #最後に残ったもの（もしくは素数）の場合はここ
        arr.append([temp, 1])
 
    if arr==[]: #1の場合はここ
        arr.append([n, 1])
 
    return arr


N,M = map(int,input().split())
A = factorization(M)
#print(A)
ans = 1
for X in A:
  if X == [1,1]:
    continue
  k = X[1]
  temp = cmb(k+N-1,k,MOD)
  ans = ans*temp%MOD
print(ans%MOD)

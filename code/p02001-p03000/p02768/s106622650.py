n,a,b=map(int,input().split())
MOD=10**9+7
def inv(a):
  return pow(a,MOD-2,MOD)

def choose(n,r):
  if r==0 or r==n:
    return 1
  else:
    A=B=1
    ls_A=[1]
    ls_B=[1]
    for i in range(r):
      A=ls_A[i]*(n-i)%MOD
      ls_A.append(A)
      B=ls_B[i]*(i+1)%MOD
      ls_B.append(B)
    return ls_A[r]*inv(ls_B[r])%MOD

def pow_k(x,n):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2 != 0:
            K=K*x%MOD
            x=x**2%MOD
            n=(n-1)//2
        else:
            x=x**2%MOD
            n=n//2%MOD
    return K*x%MOD 

print((pow_k(2,n)-1-choose(n,a)-choose(n,b))%MOD)
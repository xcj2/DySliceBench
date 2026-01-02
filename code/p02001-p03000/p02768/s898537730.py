INT_MAX=10**18+7
x=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
GETA=123
###############################################################################
import math as M
n,a,b=INPUT()
#ans=2^n-1-(n,a)-(n,b)
def power(a,n):
    if n==0:
        return 1
    else:
        if(n%2==0):
            return ((power(a,n//2))**2)%x
        else:
            return ((a%x)*(((power(a,(n-1)//2)))**2)%x)%x
def bin(n,r):
    num=1
    den=1
    for i in range(1,r+1):
        den=(den*i)%x
        num=(num*(n-i+1))%x
    return (num*power(den,x-2))%x
ans=power(2,n)-1-bin(n,a)-bin(n,b)
if ans>0:
    print(ans)
else:
    print((x+ans)%x)

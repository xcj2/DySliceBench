def modpow(a,n,p):
    if n==0:
        return 1
    x=modpow(a,n//2,p)
    x=(x*x)%p
    if (n%2)==1:
        x=(x*a)%p
    return x%p
def modinv(a,p):
    return modpow(a,p-2,p)
def choose(a,b,p,fract):#(aCb)%p
    return ((fract[a]%p)*modinv(fract[b],p)*modinv(fract[a-b],p))%p
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
add=0
sub=0
p=10**9+7
#print(A)
fract=[0]*(10**5+10)
buf=1
fract[0]=1
for i in range(1,10**5+10):
    fract[i]=(fract[i-1]*i)%p
    #print(fract[i])
for i in range(N-1,-1,-1):
    #print(A[i],i-K+2)
    if i>=K-1:
    #add=add+A[i]*(i-K+2)
        #print(i,K-1)
        #print((A[i]*choose(i,K-1,p,fract))%p)
        add=(add+(A[i]*choose(i,K-1,p,fract))%p)%p
    else:
        break
#print(add)
for i in range(0,N,1):
    if K-1<=(N-1)-i:
        #print(N-1-i, K-1)
        sub=(sub+(A[i]*choose(N-1-i,K-1,p,fract))%p)%p
    else:
        break
    #input()
print((add-sub)%p)
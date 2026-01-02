n,m=map(int,input().split())

def factorize(n):
    fct=[]
    b,e=2,0
    while b*b<=n:
        while n%b==0:
            n=n//b
            e=e+1
        if e>0:
            fct.append((b,e))
        b,e=b+1,0
    if n>1:
        fct.append((n,1))
    return fct

l=factorize(m)
mod=10**9+7
ans=1

def inv(x):
    return pow(x, mod - 2, mod)
 
cms = 10**5 + 100
cm = [0] * cms
 
def comb_init():
    cm[0] = 1
    for i in range(1, cms):
        cm[i] = cm[i-1] * i % mod
 
def c(a, b):
    return (cm[a] * inv(cm[a-b]) % mod) * inv(cm[b]) % mod

mod=10**9+7
comb_init()

for i,j in l:
    ans*=c(j+n-1,j)
    ans=ans%mod

print(ans)
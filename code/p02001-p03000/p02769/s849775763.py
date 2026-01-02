class Factorial:
    def __init__(self,n,mod):
        self.f=f=[0]*(n+1)
        f[0]=b=1
        self.mod=mod
        for i in range(1,n+1):f[i]=b=b*i%mod
        self.inv=inv=[0]*(n+1)
        inv[n]=b=pow(self.f[n],mod-2,mod)
        for i in range(n,0,-1):inv[i-1]=b=b*i%mod
    def factorial(self,i):
        return self.f[i]
    def ifactorial(self,i):
        return self.inv[i]
    def comb(self,n,k):
        if n>=k:
            return self.f[n]*self.inv[n-k]%self.mod*self.inv[k]%self.mod
        else:
            return 0
    def homp(self,n,k):
        return self.comb(n+k-1,n-1)
M=10**9+7
n,k=map(int,input().split())
f=Factorial(n*2,M)
c=f.comb
h=f.homp
a=0
for i in range(min(k+1,n)):
    a+=c(n,i)*h(n-i,i)%M
print(a%M)
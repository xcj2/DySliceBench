M=998244353
class Factorial:
    def __init__(self,n):
        self.f=f=[0]*(n+1)
        f[0]=b=1
        for i in range(1,n+1):f[i]=b=b*i%M
        self.inv=inv=[0]*(n+1)
        inv[n]=b=pow(self.f[n],M-2,M)
        for i in range(n,0,-1):inv[i-1]=b=b*i%M
    def factorial(self,i):
        return self.f[i]
    def ifactorial(self,i):
        return self.inv[i]
    def comb(self,n,k):
        if n>=k:return self.f[n]*self.inv[n-k]*self.inv[k]%M
        else:return 0
comb=Factorial(10**5*5).comb
n,m,k=map(int,input().split())
print(sum(m*comb(n-1,i)*pow(m-1,~i+n,M)for i in range(k+1))%M)
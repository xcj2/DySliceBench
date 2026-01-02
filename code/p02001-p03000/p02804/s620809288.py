class Factorial:
    def __init__(self,n,mod):
        self.f=[1]
        self.mod=mod
        for i in range(1,n+1):
            self.f.append(self.f[-1]*i%mod)
        self.i=[pow(self.f[-1],mod-2,mod)]
        for i in range(1,n+1)[::-1]:
            self.i.append(self.i[-1]*i%mod)
        self.i.reverse()
    def factorial(self,i):
        return self.f[i]
    def ifactorial(self,i):
        return self.i[i]
    def comb(self,n,k):
        return self.f[n]*self.i[n-k]%self.mod*self.i[k]%self.mod if n>=k else 0
M=10**9+7
n,k,*a=map(int,open(0).read().split())
comb=Factorial(n,M).comb
s=0
for i,a in enumerate(sorted(a)):
    s+=a*comb(i,k-1)-a*comb(~i+n,k-1)
    s%=M
print(s)
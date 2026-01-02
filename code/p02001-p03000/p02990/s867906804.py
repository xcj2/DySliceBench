class F:
    def __init__(self,n,mod):
        self.mod=mod
        self.f=[1]
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
        return 0 if k>n else self.f[n]*self.i[n-k]*self.i[k]%self.mod
n,k=map(int,input().split())
M=10**9+7
c=F(n,M).comb
for i in range(k):
    print(c(n-k+1,i+1)*c(k-1,i)%M)
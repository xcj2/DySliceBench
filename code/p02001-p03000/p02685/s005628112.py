#ライブラリの点検
class Data():
    def __init__(self):
        self.power=1
        self.rev=1     
class Combi():
    def __init__(self,N,mod):
        self.lists=[Data() for _ in range(N+1)]
        self.mod=mod  
        for i in range(2,N+1):
            self.lists[i].power=((self.lists[i-1].power)*i)%self.mod
        self.lists[N].rev=pow(self.lists[N].power,self.mod-2,self.mod)
        for j in range(N,0,-1):
            self.lists[j-1].rev=((self.lists[j].rev)*j)%self.mod
    def combi(self,K,R):
        if K<R:
            return 0
        else:
            return ((self.lists[K].power)*(self.lists[K-R].rev)*(self.lists[R].rev))%self.mod

######################
N,M,K=map(int,input().split())
mod=998244353
ans=0
C=Combi(2*10**5,mod)
for i in range(K+1):
    ans+=M*C.combi(N-1,i)*pow(M-1,N-1-i,mod)
print(ans%mod)
######################
class RollingHash():
    def __init__(self,s):
        self.length=len(s)
        self.base1=1009; self.base2=1013
        self.mod1=10**9+7; self.mod2=10**9+9
        self.hash1=[0]*(self.length+1); self.hash2=[0]*(self.length+1)
        self.pow1=[1]*(self.length+1); self.pow2=[1]*(self.length+1)
        for i in range(self.length):
            self.hash1[i+1]=(self.hash1[i]+ord(s[i]))*self.base1%self.mod1
            self.hash2[i+1]=(self.hash2[i]+ord(s[i]))*self.base2%self.mod2
            self.pow1[i+1]=self.pow1[i]*self.base1%self.mod1
            self.pow2[i+1]=self.pow2[i]*self.base2%self.mod2
    def get(self,l,r):
        h1=((self.hash1[r]-self.hash1[l]*self.pow1[r-l])%self.mod1+self.mod1)%self.mod1
        h2=((self.hash2[r]-self.hash2[l]*self.pow2[r-l])%self.mod2+self.mod2)%self.mod2
        return (h1,h2)

def solve(s,t):
    ls=len(s); lt=len(t)
    RHs=RollingHash(s*2)
    RHt=RollingHash(t)
    Judge=[False]*ls
    B=RHt.get(0,lt)
    for i in range(ls):
        if RHs.get(i,i+lt)==B:
            Judge[i]=True
    ret=0
    Visited=[-1]*ls
    for i in range(ls) :
        if Judge[i] and Visited[i]==-1:
            idx=i
            cnt=0
            while Judge[idx]:
                if Visited[idx]!=-1:
                    cnt+=Visited[idx]
                    break
                cnt+=1
                Visited[idx]=1
                idx=(idx+lt)%ls
                if idx==i:
                    return -1
            Visited[i]=cnt
            ret=max(ret,cnt)
    return ret

s=input(); t=input()
s*=(len(t)+len(s)-1)//len(s)
print(solve(s,t))
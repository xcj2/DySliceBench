class RollingHash:
    def __init__(self,S,base,M):
        self.N=len(S)
        self.M=M
        self.H=[0]*(self.N+1)
        self.B=[0]*(self.N+1)
        self.B[0]=1
        for i in range(self.N):
            self.B[i+1]=self.B[i]*base%M
            self.H[i+1]=(self.H[i]*base+(ord(S[i])-96))%M
    def get(self,l,r):
        return (self.H[r]-self.H[l]*self.B[r-l]+self.M)%self.M

def main():
    import random

    N=int(input())
    M=2**61-1
    base=random.randrange(100,M)
    RH,S=[],[]
    RH,S=[None for i in range(N)],[None]*N
    for i in range(N):
        s=input()
        S[i]=s
        RH[i]=RollingHash(s,base,M)

    dic={}
    dic[0]=[0]*26
    for k,s in enumerate(S):
        Set=set()
        l=len(s)
        for j in range(l):
            Hash=RH[k].get(j,l)
            if not Hash in dic:
                dic[Hash]=[0]*26
            for c in Set:
                dic[Hash][ord(c)-97]+=1
            Set.add(s[j])
        for c in Set:
            dic[0][ord(c)-97]+=1
    ans=0
    for i,s in enumerate(S):
        Hash=RH[i].get(1,len(s))
        ans+=dic[Hash][ord(s[0])-97]-1
    print(ans)

if __name__=='__main__':
    main()
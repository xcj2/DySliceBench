def Z_algorithm(S):
    l=len(S)
    A=[0]*l
    A[0]=l
    i=1; j=0
    while i<l:
        while i+j<l and S[j]==S[i+j]:
            j+=1
        if not j:
            i+=1
            continue
        A[i]=j
        k=1
        while l-i>k<j-A[k]:
            A[i+k]=A[k]
            k+=1
        i+=k; j-=k
    return A

def Z_find(txt,pattern):
    lp=len(pattern)
    jointxt=pattern+'-'+txt
    Z=Z_algorithm(jointxt)
    return [Z[i]==lp for i in range(lp+1,len(jointxt))]

class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
        self.size=[1]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            if self.rank[px]==self.rank[py]:
                self.rank[px]+=1
            elif self.rank[px]<self.rank[py]:
                px,py=py,px
            self.par[py]=px
            self.size[px]+=self.size[py]
    def same_check(self,x,y):
        return self.find(x)==self.find(y)

def solve(s,t):
    lt=len(t)
    s*=(lt+len(s)-1)//len(s)
    ls=len(s)
    Z=Z_find(s*2,t)
    uf=UnionFind(ls)
    loop=False
    for i in range(ls):
        if Z[i]:
            j=(i+lt)%ls
            if uf.same_check(i,j):
                return -1
            uf.union(i,j)
    return max(uf.size)-1

s=input(); t=input()
print(solve(s,t))
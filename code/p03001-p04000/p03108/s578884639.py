# ABC120D

import sys
input=sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.p=[-1]*n
        self.size=[1]*n
        
    def root(self, x):
        st=set()
        while self.p[x]>=0:
            st.add(x)
            x=self.p[x]
        for y in st:
            self.p[y]=x
        return x
    def find(self, x, y):
        return self.root(x)==self.root(y)
    def union(self, x, y):
        r1=self.root(x)
        r2=self.root(y)
        if r1==r2:
            return
        p1=self.p[r1]
        p2=self.p[r2]
        if p1<=p2:
            self.p[r2]=r1
            self.size[r1]+=self.size[r2]
            if p1==p2:
                self.p[r1]-=1
        else:
            self.p[r1]=r2
            self.size[r2]+=self.size[r1]

    
def main():
    N,M=map(int,input().split())
    AB=[tuple(map(lambda x:int(x)-1,input().split())) for i in range(M)]
    
    uft=UnionFind(N)
    ansl=[int(N*(N-1)//2)]
    for i in range(M-1,0,-1):
        a=AB[i][0]
        b=AB[i][1]
        if not uft.find(a,b):
            ansl.append(ansl[-1]-( uft.size[uft.root(a)]*uft.size[uft.root(b)] ))
        else:
            ansl.append(ansl[-1])
        uft.union(a,b)
        
    for i in range(M-1,-1,-1):
        print(ansl[i])
    
    
    
    
if __name__=="__main__":
    main()

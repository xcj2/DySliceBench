# ABC075C

import sys
input=sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.p=[-1]*n
        
    def root(self, x):
        st=[]
        while(self.p[x]>=0):
            st.append(x)
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
        up=self.p
        p1=up[r1]
        p2=up[r2]
        if p1<=p2:
            up[r2]=r1
            if p1==p2:
                up[r1]-=1
        else:
            up[r1]=r2
            
def main():
    N,M=map(int,input().split())
    AB=[tuple(map(lambda x: int(x)-1,input().split())) for i in range(M)]
    
    ans=0
    for i in range(M):
        uft=UnionFind(N)
        for j in range(M):
            if i!=j:
                uft.union(AB[j][0],AB[j][1])
        ps=0
        for x in range(N):
            if uft.p[x]<0:
                ps+=1
        if ps!=1:
            ans+=1
    print(ans)
        
    
    
    
    
if __name__=="__main__":
    main()

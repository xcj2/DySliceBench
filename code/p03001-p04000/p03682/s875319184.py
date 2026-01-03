# ABC065D

import sys
input=sys.stdin.readline
import heapq

class UnionFind:
    def __init__(self, n):
        self.p=[-1]*n
        self.size=[1]*n
    def root(self, x):
        st=set()
        while(self.p[x]>=0):
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
    N=int(input())
    r=[tuple([i]+list(map(int,input().split()))) for i in range(N)]
    rx=sorted(r,key=lambda x:x[1])
    ry=sorted(r,key=lambda x:x[2])
    pq=[]
    for i in range(1,N):
        dx=abs(rx[i][1]-rx[i-1][1])
        heapq.heappush(pq,(dx,rx[i][0],rx[i-1][0]))
        dy=abs(ry[i][2]-ry[i-1][2])
        heapq.heappush(pq,(dy,ry[i][0],ry[i-1][0]))
    uft=UnionFind(N)
    ans=0
    while(uft.size[uft.root(0)]<N):
        e=heapq.heappop(pq)
        if not(uft.find(e[1],e[2])):
            ans+=e[0]
            uft.union(e[1],e[2])
    print(ans)
    
if __name__=="__main__":
    main()

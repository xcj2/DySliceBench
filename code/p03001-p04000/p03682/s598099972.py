class UnionFind():
    def __init__(self,n):
        self.n=n
        self.root=[-1]*n
        self.rank=[-1]*n

    def Find_Root(self,x):
        if self.root[x]<0:return x
        else:
            self.root[x]=self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self,x,y):
        x=self.Find_Root(x)
        y=self.Find_Root(y)

        if x==y:return
        elif self.rank[x]>self.rank[y]:
            self.root[x] +=self.root[y]
            self.root[y]=x
        else:
            self.root[y] +=self.root[x]
            self.root[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y] +=1

    def isSameGroup(self,x,y):
        return self.Find_Root(x)==self.Find_Root(y)

    def size(self,x):
        return -self.root[self.Find_Root(x)]

    def members(self,x):
        root=self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i)==root]

    def roots(self):
        return[i for i,j in enumerate(self.root) if j<0]

    def group_members(self):
        return {i:self.members(i) for i in self.roots()}

    def group_count(self):
        return len(self.roots())


def kruskal():
    D,M=[],[]

    A,B=sorted(XY),sorted(XY, key=lambda x: x[1])
    for i in range(n-1):
        M.append([min(abs(A[i][0]-A[i+1][0]),abs(A[i][1]-A[i+1][1])),A[i][2],A[i+1][2]])
        M.append([min(abs(B[i][0]-B[i+1][0]),abs(B[i][1]-B[i+1][1])),B[i][2],B[i+1][2]])

    M.sort()
    for w,s,t in M:
        if UnionFind.isSameGroup(s,t) is False:
            UnionFind.Unite(s,t)
            D.append(w)

    return D


import sys
input=sys.stdin.readline

n=int(input())
XY=[list(map(int,input().split()))+[i+1] for i in range(n)]
UnionFind=UnionFind(n+1)
print(sum(kruskal()))
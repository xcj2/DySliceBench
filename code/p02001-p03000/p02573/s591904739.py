class UFtree:
    def __init__(self,length):
        self.N=length
        self.tree=[-1 for i in range(length)]
        self.rank=[0 for i in range(length)]
    def find(self,X):
        if self.tree[X]<0:
            return X
        XX=self.find(self.tree[X])
        self.tree[X]=XX
        return XX

    def unite(self,X,Y):
        X=self.find(X)
        Y=self.find(Y)

        if Y==X:
            return

        if self.rank[X]>self.rank[Y]:
            self.tree[X]+=self.tree[Y]
            self.tree[Y]=X
        else:
            if self.rank[Y]==self.rank[X]:
                self.rank[Y]+=1
            self.tree[Y]+=self.tree[X]
            self.tree[X]=Y



def resolve():
    N,M = map(int,input().split())
    ut = UFtree(N)
    for i in range(M):
        A,B = map(int,input().split())
        ut.unite(A-1,B-1)

    print(-1*min(ut.tree))
resolve()

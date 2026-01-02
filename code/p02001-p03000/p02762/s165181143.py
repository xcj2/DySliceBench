import sys
input=sys.stdin.readline
class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)] #親要素のノード番号を格納
        self.rank=[0]*n #木の高さを格納
        self.size=[1]*n #size[i]:iを根とするグループのサイズ
    def find(self,x): #根を検索
        if self.par[x]==x: #par[x]==xの時そのノードは根
            return x
        else:
            self.par[x]=self.find(self.par[x]) #親を書き換える
            return self.par[x]
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            if self.rank[px]==self.rank[py]: #木の高さが同じなら親とする方を1増やす
                self.rank[px]+=1
            elif self.rank[px]<self.rank[py]:
                px,py=py,px #木の高さが高い方をpxとする
            self.par[py]=px #木の高さが高い方を親とする
            self.size[px]+=self.size[py]
    def same_check(self,x,y): #同じ木に属するか判定
        return self.find(x)==self.find(y)
    
def main():
    n,m,k=map(int,input().split())
    uf=UnionFind(n)
    F_edges=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        a-=1; b-=1
        uf.union(a,b)
        F_edges[a].append(b)
        F_edges[b].append(a)
    B=[0]*n
    for _ in range(k):
        a,b=map(int,input().split())
        a-=1; b-=1
        if uf.same_check(a,b):
            B[a]+=1
            B[b]+=1
    Ans=[]
    for i in range(n):
        Ans.append(uf.size[uf.find(i)]-1-len(F_edges[i])-B[i])
    print(*Ans)
    
if __name__=='__main__':
    main()
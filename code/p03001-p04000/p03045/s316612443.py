class UnionFold:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        
        #木の高さを格納する（初期状態では０）
        self.rank = [0]*(n+1)
        
    def find(self, x):
        #根ならその番号を返す
        if self.par[x]==x:
            return x
        
        #根でないないなら親の要素で再検索
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])
    
    #同じ木に属するか判定
    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    #併合
    def union(self,x,y):
        #根を探す
        x = self.find(x)
        y = self.find(y)
        
        #木の高さを比較し、低い方から高い方に辺を繋ぐ
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
                
def main():
    N,M = map(int, input().split())
    union_fold = UnionFold(N)
    for _ in range(M):
        x,y,z = map(int, input().split())
        if not(union_fold.same(x,y)):
            union_fold.union(x,y)
    
    n=0
    for i in range(1,N+1):
        if union_fold.par[i]==i:
            n+=1
    print(n)
    
main()
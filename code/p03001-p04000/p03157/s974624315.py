

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    ################
    class UnionFind():
        """
        parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
        find(x):要素xの属するグループの根を返す
        size(x):要素xの属するグループの要素数を返す
        same(x,y):x,yが同じグループに属しているか返す
        members(x):要素xが属するグループに属する要素をリストで返す
        roots:全ての根の要素を返す
        group_count():グループの数を返す
        all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
        """
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            #根を探す&つなぎかえる
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
        
    ################

    H,W=MI()
    S=[]
    for i in range(H):
        s=input()
        S.append(s)
    uf=UnionFind(H*W)
    
    dx=[0,1]
    dy=[1,0]
    
    def make(ii,jj):
        return ii*W+jj
    

    
    for i in range(H):
        for j in range(W):
            for k in range(2):
                ni=i+dx[k]
                nj=j+dy[k]
                if 0<=ni<H and 0<=nj<W:
                    if S[i][j]!=S[ni][nj]:
                        uf.union(make(i,j),make(ni,nj))
                        
    ans=0
    from collections import defaultdict
    ddb = defaultdict(int)
    ddh = defaultdict(int)
    
    for i in range(H):
        for j in range(W):
            v=make(i,j)
            root=uf.find(v)
            if S[i][j]=="#":
                ddb[root]+=1
            else:
                ddh[root]+=1
                
    for k,v in ddb.items():
        ans+=v*ddh[k]

        
        
    print(ans)
            
    
        
main()

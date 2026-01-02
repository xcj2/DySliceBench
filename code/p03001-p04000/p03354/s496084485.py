import sys
input=sys.stdin.readline

class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n

    def find(self,x): #根を見つける、繋ぎ直す
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self,x,y): #x,yの含むグループを併合する
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return
        
        if self.parents[x]>self.parents[y]:
            x,y=y,x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    
    def same(self,x,y):#xとyが同じグループにいるか判定
        return self.find(x)==self.find(y)
    
    def members(self,x):#xと同じグループのメンバーを列挙
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]
    
    def size(self,x):#xが属するグループのメンバーの数
        return -self.parents[self.find(x)]
    
    def roots(self):#ufの根を列挙
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):#グループの数を数える
        return len(self.roots())

    def all_group_members(self):#根:メンバの辞書を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):#print()での表示用
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    n,m = map(int,input().split())
    p = [int(i)-1 for i in input().split()]
    dic = {i:idx for idx,i in enumerate(p)}   

    uf = UnionFind(n)
    for _ in range(m):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        uf.unite(x,y)
    
    cnt = 0
    for i in range(n):
        if uf.same(dic[i],i):
            cnt += 1
    
    print(cnt)  
  
if __name__=='__main__':
    main()

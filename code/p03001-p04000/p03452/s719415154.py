from collections import*
class POTENTIAL_UNION_FIND(object):
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]#非負なら親ノード，負ならグループの要素数
        self.diff_p = [0 for i in range(n)]#親ノードを基準としたポテンシャル
 
    def root(self, x): #root(x): xの根ノードを返す
        if self.parent[x] < 0:
            return x
        else:
            rx = self.root(self.parent[x]) #xをxの根rxに直接つなぎたい
            self.diff_p[x] += self.diff_p[self.parent[x]] #そのために，diff(rx,x)を計算
            self.parent[x] = rx #xをrxに直接つなげる
            return rx
 
    def size(self,x): #size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]

    def merge(self, x, y, dxy): #ポテンシャル差の条件p(y)-p(x)=dxyでxとyのグループをまとめる
        rx = self.root(x) #rxを新たにxと名づける
        ry = self.root(y) #ryを新たにyと名づける
        dxy += self.diff_p[x] - self.diff_p[y] #dxyをdiff(rx,ry)で置き換え
        x,y=rx,ry
        if x == y:
            return False
        if self.parent[x] > self.parent[y]: #xの要素数がyの要素数より「小さい」とき入れ替える
            x,y,dxy=y,x,-dxy
        self.parent[x] += self.parent[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        self.diff_p[y] = dxy #yの相対ポテンシャルを更新
        return True
 
    def issame(self, x, y): #issame(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)
        
    def diff(self,x,y): #diff(x,y): xを基準としたyのポテンシャルを返す 
        if self.root(x) == self.root(y): #この時点でxの親はroot(x)
            return self.diff_p[y] - self.diff_p[x]
        else:
            return None


n,m=map(int,input().split())
u=POTENTIAL_UNION_FIND(n)
d=defaultdict(int)
for i in range(m):
    a,b,c=map(int,input().split())
    d[(a-1,b-1)]=c
    u.merge(a-1,b-1,c)
for k,v in d.items():
    if v!=u.diff(*k):
        print("No")
        exit()
print("Yes")
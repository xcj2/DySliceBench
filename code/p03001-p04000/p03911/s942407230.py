import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
うーん，二部グラフっぽい？
言語と人の対応で，パスが8以内にあればOKみたいな
木の直径みたいな感じで行ける？
ある人から見て一番遠い人を1人選んで，その人から見て全員が8以内に入ればOKそう？
誤読っぽ，単純にUFで良いかも
"""

def main():
    ################
    class UnionFind():
        """
        parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
        find(x):要素xの属するグループの根を返す
        size(x):要素xの属するグループの要素数を返す
        same(x,y):x,yが同じグループに属しているか返す
        重いかも！　　members(x):要素xが属するグループに属する要素をリストで返す
        roots:全ての根の要素を返す
        group_count():グループの数を返す
        重いかも！　all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
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


    
    N,M=MI()
    uf=UnionFind(N+M)
    for i in range(N):
        L=LI()
        for j in range(1,L[0]+1):
            l=L[j]
            l-=1
            uf.union(i,l+N)
            
    roots=uf.roots()
    temp=0
    for v in roots:
        if v<N:
            temp+=1
        
            
    if temp<=1:
        print("YES")
    else:
        print("NO")
        

        
            
    
main()

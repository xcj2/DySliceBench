import sys
input = sys.stdin.readline

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
    mod=10**9+7
    N=I()
    A=LI()
    B=LI()
    
    A,B=zip(*sorted(zip(A,B)))
    
    
    #基本的にBを恥からソートしてもN-1回，完全逆順とかならそれはそれで楽にソートできるので，
    #結局はBをソートするだけの話? 流石に違う気もするが...
    #=>A:1,2,3,4,5
    #  B:5,1,2,3,4みたいなケースが無理になるのか2,3,4,5,1もダメ．でも2,3,4,5,2はOK
    
    #普通にB:4,5,1,2,3みたいなのもダメ，Bが輪になっているとダメか
    #Bがある地点から昇順になるなら，つなげば1つのグループができる
    
    A1=sorted(A)
    B1=sorted(B)
    
    from collections import defaultdict
    dd = defaultdict(int)
    
    #Bの数字と順番を対応させる．Bないにかぶりがあるときはflag2で引っかかるはず?
    
    for i in range(N):
        dd[B1[i]]=i
    
    flag=1
    
    #回数制限なしでできるか
    for i in range(N):
        if B1[i]<A1[i]:
            flag=0
            break
        
    flag2=0#sortずみのB[i]を1箇所ずらしても条件を満たしうるか，これが1ならOK
    
    for i in range(N-1):
        if B1[i]>=A1[i+1]:
            flag2=1
            break
        
    flag3=0#巡回かどうか
    uf=UnionFind(N)
    
    for i in range(N):
        a=dd[B[i]]
        b=dd[B1[i]]
        uf.union(a,b)
    
    if uf.group_count()==1:
        flag3=1
        
    if flag2==0 and flag3:
        flag=0
        
        
    if flag==1:
        print("Yes")
    else:
        print("No")
    
  
    

main()
